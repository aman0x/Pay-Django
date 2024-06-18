from rest_framework import viewsets, permissions, status
from .serializers import InvoiceSerializer
from invoiceApp.models import Invoice

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]