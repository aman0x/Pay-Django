from rest_framework import viewsets, permissions, status, generics
from userApp.models import CustomUser, Kyc, BankAccount, Beneficiary
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from django.conf import settings
from firebase_admin import auth
from .serializers import RegisterSerializer, KycSerializer, EmailLoginSerializer, OTPRequestSerializer, UserProfileSerializer,BankAccountSerializer, BeneficiarySerializer, FirebaseIDTokenSerializer, OTPVerifySerializer

from utils.utils import send_otp, verify_otp
from rest_framework.views import APIView
from userApp.permissions import IsOwnerOrAdder
from rest_framework.exceptions import NotFound
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


from firebase_admin import auth




common_status = settings.COMMON_STATUS

class BeneficiaryCreateView(generics.CreateAPIView):
    serializer_class = BeneficiarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BeneficiaryUpdateBankView(generics.GenericAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Beneficiary.objects.none()  # Dummy queryset

    def get_beneficiary(self):
        user = self.request.user
        beneficiary_id = self.kwargs['pk']
        try:
            return Beneficiary.objects.get(user=user, id=beneficiary_id)
        except Beneficiary.DoesNotExist:
            raise NotFound('Beneficiary not found')

    def get(self, request, *args, **kwargs):
        beneficiary = self.get_beneficiary()
        if not beneficiary.bank_account:
            raise NotFound('No bank account associated with this beneficiary.')
        serializer = self.get_serializer(beneficiary.bank_account)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        beneficiary = self.get_beneficiary()
        if beneficiary.bank_account:
            return Response({'detail': 'Bank account already associated with this beneficiary.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bank_account = serializer.save(user=request.user)
        beneficiary.bank_account = bank_account
        beneficiary.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        beneficiary = self.get_beneficiary()
        if not beneficiary.bank_account:
            raise NotFound('No bank account associated with this beneficiary.')
        serializer = self.get_serializer(beneficiary.bank_account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ListBeneficiariesView(generics.ListAPIView):
    serializer_class = BeneficiarySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone_number']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        return Beneficiary.objects.filter(user=user, deleted=False)

class BeneficiaryDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user = request.user
        try:
            beneficiary = Beneficiary.objects.get(user=user, id=pk)
        except Beneficiary.DoesNotExist:
            raise NotFound('Beneficiary not found')
        
        beneficiary.deleted = True
        beneficiary.save()
        return Response({"detail": "Beneficiary marked as deleted"}, status=status.HTTP_204_NO_CONTENT)


class BankAccountListView(generics.ListAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['account_name', 'account_number', 'bank_name']

    def get_queryset(self):
        user = self.request.user
        return BankAccount.objects.filter(user=user, deleted=False)

# Create a new bank account
class BankAccountCreateView(generics.CreateAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Mark a bank account as deleted instead of removing it
class BankAccountDeleteView(generics.UpdateAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdder]
    queryset = BankAccount.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

# Retrieve a single bank account instance
class BankAccountDetailView(generics.RetrieveAPIView):
    queryset = BankAccount.objects.filter(deleted=False)
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdder]




class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("id")
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class KycViewSet(viewsets.ModelViewSet):
    queryset = Kyc.objects.all().order_by("id")
    serializer_class = KycSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]



class EmailLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = EmailLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FirebaseGoogleLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = FirebaseIDTokenSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data
            try:
                user = CustomUser.objects.get(social_login_uid=uid)
            except CustomUser.DoesNotExist:
                firebase_user = auth.get_user(uid)
                user = CustomUser.objects.create(
                    email=firebase_user.email,
                    first_name=firebase_user.display_name,
                    social_login_uid=uid,
                    is_social_login=True
                )
                user.set_unusable_password()
                user.save()
                
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class OTPRequestView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('phone')
            if not CustomUser.objects.filter(phone=phone).exists():
                return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
            response = send_otp(phone)
            if response and response.get('Status') == 'Success':
                return Response({'session_id': response.get('Details')}, status=status.HTTP_200_OK)
            return Response({'error': 'Failed to send OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OTPVerifyView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('phone')
            otp = serializer.validated_data.get('otp')
            session_id = serializer.validated_data.get('session_id')
            response = verify_otp(session_id, otp)
            if response and response.get('Status') == 'Success':
                try:
                    user = CustomUser.objects.get(phone=phone)
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user_id': user.id
                    }, status=status.HTTP_200_OK)
                except CustomUser.DoesNotExist:
                    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)