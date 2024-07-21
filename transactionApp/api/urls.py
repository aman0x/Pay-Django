from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transactionApp.views import TransactionViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls)),
]
