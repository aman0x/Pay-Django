from rest_framework import viewsets, permissions, status
from .serializers import BankAccountSerializer, BeneficiarySerializer
from accountApp.models import BankAccount, Beneficiary

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
class BeneficiaryViewSet(viewsets.ModelViewSet):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]