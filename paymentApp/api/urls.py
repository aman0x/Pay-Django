from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'data', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', views.PaymentDashboardViewSet.as_view(), name="payment-dashboard"),
    path('all-payments/', views.PaymentAllPaymentsViewSet.as_view(), name="payment-dashboard"),
    path('payment-details/', views.PaymentDetailsViewSet.as_view(), name="payment-details"),
]
