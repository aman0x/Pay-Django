from rest_framework import viewsets, permissions, status, views, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from invoiceApp.models import Invoice, Service
from rest_framework.response import Response
from .filters import InvoiceFilter


from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import InvoiceSerializer, ServiceSerializer
from invoiceApp.models import Invoice, Service
from rest_framework.permissions import IsAuthenticated

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = InvoiceFilter
    search_fields = ['invoice_number']
    ordering_fields = ['created_at', 'amount', 'status']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



class RaisedInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'created_at']
    search_fields = ['beneficiary__name', 'invoice_number']
    ordering_fields = ['created_at', 'amount', 'status']

class PayableInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(beneficiary__user=self.request.user)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'created_at']
    search_fields = ['user__username', 'invoice_number']
    ordering_fields = ['created_at', 'amount', 'status']


    
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
            "bank": "HDFC Bank , KODAD, HDFC0001642",
            "account_type": "Current",
            "transaction_id" : "TD1711364044252",
            "status" : "Succeeded",
            "sum": 23000.56
        }
        serializer = InvoiceAllInvoiceSerializer(data)
        return Response(serializer.data)
    
class InvoiceDetailsViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "status" : "In Progress",
            "invoice_title" : "Vendor_Payment",
            "invoice_id" : "TD1711364044252",
            "date" : "2024-06-21T10:21:17.116232Z",
            "particulars" : "Vendor_Payment",
            "quantity" : 1,
            "price_per_quantity" : 24000.24,
            "amount" : 24000.24,
            "gst" : 20,
            "subtotal" : 24000.24,
            "name" : "ANANTHARAPU ARUNA THEJASWINI",
            "phone_number" : "+919573749630",
            "email" : "customer@mail.com",
            "account_number" : "50100350093919",
            "bank" : "HDFC Bank",
            "bank_branch" : "KODAD",
            "ifsc_code" : "HDFC0001642",
            "total_amount" : 24000.24,
        }
        serializer = InvoiceDetailsSerializer(data)
        return Response(serializer.data)
    
class InvoiceNewInvoicesViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "invoice_title" : "Vendor_Payment",
            "invoice_id" : "TD1711364044252",
            "date" : "2024-06-21T10:21:17.116232Z",
            "name" : "ANANTHARAPU ARUNA THEJASWINI",
            "bank" : "HDFC Bank",
            "bank_branch" : "KODAD",
            "ifsc_code" : "HDFC0001642",
            "total_amount" : 24000.24,
        }
        serializer = InvoiceNewInvoicesSerializer(data)
        return Response(serializer.data)