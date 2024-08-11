
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *


urlpatterns = [
    path('login/email/', EmailLoginView.as_view(), name='email_login'),
    path('api/google-login/', FirebaseGoogleLoginView.as_view(), name='google-login'),
    path('otp/request/', OTPRequestView.as_view(), name='otp_request'),
    path('otp/verify/', OTPVerifyView.as_view(), name='otp_verify'),
    
    
    #retry #reset password #register
    
    #register
    path('register/step-one/', UserRegistrationStepOneView.as_view(), name='register-step-one'),
    path('verify-otp-register/', OTPVerificationView.as_view(), name='verify-otp'),
    path('complete-registration/', CompleteRegistrationView.as_view(), name='complete-registration'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    
    #new working 
    path('bank-accounts/', BankAccountListView.as_view(), name='bank-account-list'),
    path('bank-accounts/add/', BankAccountCreateView.as_view(), name='bank-account-create'),
    path('bank-accounts/<int:pk>/', BankAccountDetailView.as_view(), name='bank-account-detail'),
    path('bank-accounts/<int:pk>/delete/', BankAccountDeleteView.as_view(), name='bank-account-delete'),
    
    path('beneficiaries/', ListBeneficiariesView.as_view(), name='beneficiary-list'),
    path('beneficiaries/create/', BeneficiaryCreateView.as_view(), name='beneficiary-create'),
    path('beneficiaries/<int:pk>/update-bank/', BeneficiaryUpdateBankView.as_view(), name='beneficiary-update-bank'),
    path('beneficiaries/<int:pk>/delete/', BeneficiaryDeleteView.as_view(), name='beneficiary-delete'),
]
