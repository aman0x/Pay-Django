from rest_framework import serializers
from userApp.models import CustomUser, Kyc

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields= "__all__"
        
class KycSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kyc
        fields= "__all__"