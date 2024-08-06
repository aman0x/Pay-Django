from rest_framework import serializers
from userApp.models import CustomUser, Kyc, CustomUser, BankAccount, Beneficiary
from django.contrib.auth import authenticate
from firebase_admin import auth


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ['id', 'user', 'name', 'phone_number', 'bank_account',  "verified", "verified_at", 'created_at', 'deleted']
        ref_name = 'UserAppBeneficiarySerializer' 
        read_only_fields = ['id', 'user', 'bank_account']

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'user', 'account_name', 'account_number', 'ifsc_code', 'account_type', 'account_type_2', 'gstin', 'pan', 'bank_name', 'deleted']
        ref_name = 'UserAppBankAccountSerializer' 
        read_only_fields = ['id', 'user']



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'nick_name', 'email', 'phone', 'pan_no', 'adhaar_no', 'account_type', 'company_name', 'company_pan_no', 'company_adhaar_no']
        read_only_fields = ['email']  
    
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


class FirebaseIDTokenSerializer(serializers.Serializer):
    id_token = serializers.CharField(write_only=True)

    def validate(self, data):
        id_token = data.get('id_token')
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            return uid
        except Exception as e:
            raise serializers.ValidationError("Invalid ID token")


class OTPRequestSerializer(serializers.Serializer):
    phone = serializers.CharField()

class OTPVerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp = serializers.CharField()
    session_id = serializers.CharField()

