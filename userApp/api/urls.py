from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'data', views.CustomUserViewSet)
router.register(r'kyc', views.KycViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
