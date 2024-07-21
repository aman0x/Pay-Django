from rest_framework import viewsets, permissions, status
from .serializers import RegisterSerializer, KycSerializer
from userApp.models import CustomUser, Kyc
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from django.conf import settings
from firebase_admin import auth
from .firebase_init import initialize_firebase
from .serializers import EmailLoginSerializer, OTPLoginSerializer
from rest_framework.views import APIView




common_status = settings.COMMON_STATUS


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