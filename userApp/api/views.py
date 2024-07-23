from rest_framework import viewsets, permissions, status, generics
from userApp.models import CustomUser, Kyc, BankAccount, Beneficiary
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from django.conf import settings
from firebase_admin import auth
from .firebase_init import initialize_firebase
from .serializers import RegisterSerializer, KycSerializer, EmailLoginSerializer, OTPLoginSerializer, UserProfileSerializer,BankAccountSerializer, BeneficiarySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from userApp.permissions import IsOwnerOrAdder
from rest_framework.exceptions import NotFound




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

    def get_queryset(self):
        user = self.request.user
        return Beneficiary.objects.filter(user=user)


# List all bank accounts for the authenticated user
class BankAccountListView(generics.ListAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BankAccount.objects.filter(user=user)


# Create a new bank account
class BankAccountCreateView(generics.CreateAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# List all bank accounts added by the authenticated user
class AllAddedBankAccountsView(generics.ListAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BankAccount.objects.filter(added_by=user)

# Retrieve a single bank account instance
class BankAccountDetailView(generics.RetrieveAPIView):
    queryset = BankAccount.objects.all()
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
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = OTPLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
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