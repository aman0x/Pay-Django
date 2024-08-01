from django_filters import rest_framework as filters
from invoiceApp.models import Invoice

class InvoiceFilter(filters.FilterSet):
    user_username = filters.CharFilter(method='filter_by_user_username')
    beneficiary_name = filters.CharFilter(method='filter_by_beneficiary_name')

    class Meta:
        model = Invoice
        fields = ['user_username', 'beneficiary_name', 'status', 'created_at']

    def filter_by_user_username(self, queryset, name, value):
        return queryset.filter(user__username__icontains=value)

    def filter_by_beneficiary_name(self, queryset, name, value):
        return queryset.filter(beneficiary__name__icontains=value)
