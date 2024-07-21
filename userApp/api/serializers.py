from rest_framework import serializers
from userApp.models import CustomUser, Kyc, CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields= "__all__"
        
class KycSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kyc
        fields= "__all__"
        

class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

class OTPLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp = serializers.CharField(write_only=True)

    def validate(self, data):
        phone = data.get('phone')
        otp = data.get('otp')
        try:
            user = CustomUser.objects.get(phone=phone, otp=otp)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or phone number")
        return user
