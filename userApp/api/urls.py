from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'register', views.RegisterViewSet)
router.register(r'kyc', views.KycViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view(), name="login"),
    path('verify-otp/', views.VerifyOTPView.as_view(), name="verify-otp"),
]
