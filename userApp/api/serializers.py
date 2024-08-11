from django.conf import settings
from rest_framework import serializers
from userApp.models import CustomUser, Kyc, CustomUser, BankAccount, Beneficiary, IndividualUser, BusinessUser
from django.contrib.auth import authenticate
from firebase_admin import auth
import random
import requests


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'nick_name', 'phone', 'account_type', 'profile_image']

class IndividualUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualUser
        fields = ['pan_no', 'pan_no_doc', 'adhaar_no', 'adhaar_front_doc', 'adhaar_back_doc']

class BusinessUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = ['company_name', 'company_pan_no', 'company_pan_no_doc', 'company_adhaar_no', 'company_gst_no', 'company_gst_no_doc']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'nick_name', 'phone', 'account_type', 'profile_image']

class IndividualUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualUser
        fields = ['pan_no', 'pan_no_doc', 'adhaar_no', 'adhaar_front_doc', 'adhaar_back_doc']

class BusinessUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = ['company_name', 'company_pan_no', 'company_pan_no_doc', 'company_adhaar_no', 'company_gst_no', 'company_gst_no_doc']

class CompleteRegistrationSerializer(serializers.Serializer):
    individual_user = IndividualUserSerializer(required=False)
    business_user = BusinessUserSerializer(required=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def save(self, user):
        individual_data = self.validated_data.pop('individual_user', None)
        business_data = self.validated_data.pop('business_user', None)
        password = self.validated_data.pop('password')

        user.set_password(password)
        user.save()

        if user.account_type == 'INDIVIDUAL' and individual_data:
            IndividualUser.objects.update_or_create(user=user, defaults=individual_data)
        elif user.account_type == 'BUSINESS' and business_data:
            BusinessUser.objects.update_or_create(user=user, defaults=business_data)

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    individual_user = IndividualUserSerializer(required=False)
    business_user = BusinessUserSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'nick_name', 'phone', 'account_type', 'profile_image', 'individual_user', 'business_user']

    def update(self, instance, validated_data):
        individual_data = validated_data.pop('individual_user', None)
        business_data = validated_data.pop('business_user', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if instance.account_type == 'INDIVIDUAL' and individual_data:
            IndividualUser.objects.update_or_create(user=instance, defaults=individual_data)
        elif instance.account_type == 'BUSINESS' and business_data:
            BusinessUser.objects.update_or_create(user=instance, defaults=business_data)

        return instance
    
class UserRegistrationStepOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'phone']

    def validate_phone(self, value):
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return value

    def create(self, validated_data):
        user = CustomUser(
            first_name=validated_data['first_name'],
            middle_name=validated_data.get('middle_name', ''),
            last_name=validated_data['last_name'],
            phone=validated_data['phone']
        )
        user.set_unusable_password()  # Set a temporary unusable password
        user.otp = settings.DEFAULT_TEST_OTP if settings.TEST_MODE else random.randint(100000, 999999)  # Use test OTP in test mode
        user.save()

        # Send the OTP to the user's phone number via 2Factor API
        if not settings.TEST_MODE:
            self.send_otp(user.phone, user.otp)

        return user

    def send_otp(self, phone, otp):
        url = f"https://2factor.in/API/V1/{settings.TWO_FACTOR_API_KEY}/SMS/{phone}/{otp}"
        response = requests.get(url)
        response_data = response.json()
        if response_data['Status'] != 'Success':
            raise serializers.ValidationError("Failed to send OTP. Please try again.")


class OTPVerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    otp = serializers.IntegerField()

    def validate(self, data):
        phone = data.get('phone')
        otp = data.get('otp')

        user = CustomUser.objects.filter(phone=phone).first()
        if not user:
            raise serializers.ValidationError("User with this phone number does not exist.")

        # Verify the OTP via 2Factor API or check against default OTP in test mode
        if not self.verify_otp(phone, otp):
            raise serializers.ValidationError("Invalid OTP.")

        return data

    def verify_otp(self, phone, otp):
        if settings.TEST_MODE and otp == settings.DEFAULT_TEST_OTP:
            return True

        url = f"https://2factor.in/API/V1/{settings.TWO_FACTOR_API_KEY}/SMS/VERIFY/{otp}/{phone}"
        response = requests.get(url)
        response_data = response.json()
        return response_data['Status'] == 'Success'

    def save(self):
        phone = self.validated_data.get('phone')
        user = CustomUser.objects.get(phone=phone)
        user.otp = None  # Clear OTP after successful verification
        user.save()
        return user

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

