
from django.urls import path
from .views import EmailLoginView, OTPLoginView, LogoutView

urlpatterns = [
    path('login/email/', EmailLoginView.as_view(), name='email_login'),
    path('login/otp/', OTPLoginView.as_view(), name='otp_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
