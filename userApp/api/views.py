from rest_framework import viewsets, permissions, status
from .serializers import CustomUserSerializer, KycSerializer
from userApp.models import CustomUser, Kyc

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
class KycViewSet(viewsets.ModelViewSet):
    queryset = Kyc.objects.all()
    serializer_class = KycSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]