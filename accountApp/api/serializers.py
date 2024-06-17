from rest_framework import serializers
from accountApp.models import BankAccount, Beneficiary

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankAccount
        fields= "__all__"
        
class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Beneficiary
        fields= "__all__"