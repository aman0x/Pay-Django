
from django.urls import path
from .views import EmailLoginView, OTPLoginView, LogoutView, UserProfileView, BankAccountCreateView, BankAccountListView,  BankAccountDetailView, BeneficiaryCreateView, ListBeneficiariesView,BeneficiaryUpdateBankView, BankAccountDeleteView

urlpatterns = [
    path('login/email/', EmailLoginView.as_view(), name='email_login'),
    path('login/otp/', OTPLoginView.as_view(), name='otp_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    
    path('bank-accounts/', BankAccountListView.as_view(), name='bank-account-list'),
    path('bank-accounts/add/', BankAccountCreateView.as_view(), name='bank-account-create'),
    path('bank-accounts/<int:pk>/', BankAccountDetailView.as_view(), name='bank-account-detail'),
    path('bank-accounts/<int:pk>/delete/', BankAccountDeleteView.as_view(), name='bank-account-delete'),
    
    path('beneficiaries/', BeneficiaryCreateView.as_view(), name='create_beneficiary'),
    path('beneficiaries/<int:pk>/update-bank/', BeneficiaryUpdateBankView.as_view(), name='update_beneficiary_bank'),
    path('beneficiaries/list/', ListBeneficiariesView.as_view(), name='list_beneficiaries'),
]
