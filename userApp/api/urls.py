
from django.urls import path
from .views import EmailLoginView, OTPLoginView, LogoutView, UserProfileView, BankAccountCreateView, BankAccountListView, AllAddedBankAccountsView, BankAccountDetailView

urlpatterns = [
    path('login/email/', EmailLoginView.as_view(), name='email_login'),
    path('login/otp/', OTPLoginView.as_view(), name='otp_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('bank-accounts/', BankAccountListView.as_view(), name='list_bank_accounts'),
    path('bank-accounts/add/', BankAccountCreateView.as_view(), name='create_bank_account'),
    path('bank-accounts/added/', AllAddedBankAccountsView.as_view(), name='all_added_bank_accounts'),
    path('bank-accounts/<int:pk>/', BankAccountDetailView.as_view(), name='detail_bank_account'),
]
