from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bank', views.BankAccountViewSet)
router.register(r'beneficiary', views.BeneficiaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
