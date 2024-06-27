from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('transaction-dashboard/', views.StatisticTransactionDashboardViewSet.as_view(), name="statistic-transaction-dashboard"),
    path('invoice-sent-dashboard/', views.StatisticInvoiceSentDashboardViewSet.as_view(), name="statistic-invoice-sent-dashboard"),
    path('invoice-received-dashboard/', views.StatisticInvoiceReceivedDashboardViewSet.as_view(), name="statistic- invoice-received-dashboard"),
    path('transaction-list/', views.StatisticTransactionListViewSet.as_view(), name="statistic-transaction-list"),
    path('invoice-sent-list/', views.StatisticTransactionListViewSet.as_view(), name="statistic-invoice-sent-list"),
    path('invoice-received-list/', views.StatisticTransactionListViewSet.as_view(), name="statistic-invoice-received-list"),
]
