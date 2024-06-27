from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('transaction-dashboard/', views.StatisticTransactionDashboardViewSet.as_view(), name="statistic-transaction-dashboard"),
    path('invoice-sent-dashboard/', views.StatisticTransactionDashboardViewSet.as_view(), name="invoice-sent-dashboard"),
    path('invoice-received-dashboard/', views.StatisticTransactionDashboardViewSet.as_view(), name="invoice-received-dashboard"),
]
