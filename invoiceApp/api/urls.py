from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'data', views.InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sent-dashboard/', views.InvoiceSentDashboardViewSet.as_view(), name="invoice-sent-dashboard"),
    path('received-dashboard/', views.InvoiceReceivedDashboardViewSet.as_view(), name="invoice-received-dashboard"),
    path('all-invoices/', views.InoviceAllInvoiceViewSet.as_view(), name="all-invoices"),
]
