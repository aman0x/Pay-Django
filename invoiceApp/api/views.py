from rest_framework import viewsets, permissions, status, views
from .serializers import *
from invoiceApp.models import Invoice
from rest_framework.response import Response

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
class InvoiceSentDashboardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "all_invoices" : 1200,
            "successful" : 12,
            "in_progress" : 122,
            "failed" : 123,
            "refunded" : 123,
            "today_successful" : 4,
            "today_in_progress" : 1,
            "today_failed" : 2,
            "today_refunded" : 0,
        }
        serializer = InvoiceSentDashboardSerializer(data)
        return Response(serializer.data)
    
class InvoiceReceivedDashboardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "all_invoices" : 1200,
            "successful" : 12,
            "in_progress" : 122,
            "failed" : 123,
            "refunded" : 123,
            "today_successful" : 4,
            "today_in_progress" : 1,
            "today_failed" : 2,
            "today_refunded" : 0,
        }
        serializer = InvoiceSentDashboardSerializer(data)
        return Response(serializer.data)
    
class InoviceAllInvoiceViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "recipient": "ANANTHARAPU ARUNA THEJASWINI",
            "type" : "Vendor_Payment",
            "bank": "HDFC Bank",
            "account_type": "Current",
            "transaction_id" : "TD1711364044252",
            "status" : "Succeeded",
            "sum": 23000.56
        }
        serializer = InvoiceAllInvoiceSerializer(data)
        return Response(serializer.data)