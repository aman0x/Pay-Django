from django_filters import rest_framework as filters
from invoiceApp.models import Invoice

class InvoiceFilter(filters.FilterSet):
    user__username = filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    beneficiary__name = filters.CharFilter(field_name='beneficiary__name', lookup_expr='icontains')
    
    class Meta:
        model = Invoice
        fields = {
            'status': ['exact'],
            'created_at': ['exact', 'gte', 'lte'],
            'amount': ['exact', 'gte', 'lte'],
            'invoice_number': ['icontains'],
        }
