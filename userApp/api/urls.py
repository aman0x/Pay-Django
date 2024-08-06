
from django.urls import path
from .views import EmailLoginView, OTPLoginView, LogoutView, UserProfileView, BankAccountCreateView, BankAccountListView,  BankAccountDetailView, BeneficiaryCreateView, ListBeneficiariesView,BeneficiaryUpdateBankView, BankAccountDeleteView, BeneficiaryDeleteView

urlpatterns = [
    path('login/email/', EmailLoginView.as_view(), name='email_login'),
    
    path('login/otp/', OTPLoginView.as_view(), name='otp_login'),
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
