from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'raised-invoices', views.RaisedInvoiceViewSet, basename='raised-invoices')
router.register(r'payable-invoices', views.PayableInvoiceViewSet, basename='payable-invoices')

urlpatterns = [
    path('', include(router.urls)),
    # path('sent-dashboard/', views.InvoiceSentDashboardViewSet.as_view(), name="invoice-sent-dashboard"),
    # path('received-dashboard/', views.InvoiceReceivedDashboardViewSet.as_view(), name="invoice-received-dashboard"),
    # path('all-invoices/', views.InoviceAllInvoiceViewSet.as_view(), name="all-invoices"),  # Corrected name
    # path('invoice-details/', views.InvoiceDetailsViewSet.as_view(), name="invoice-details"),
    # path('new-invoices/', views.InvoiceNewInvoicesViewSet.as_view(), name="new-invoices"),
]
