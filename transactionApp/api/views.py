from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from transactionApp.models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['transaction_amount', 'beneficiary', 'transaction_type', 'created_at', 'services']
    search_fields = ['beneficiary__name', 'services__name', 'card__card_holder_name', 'bank_account__account_name']
    ordering_fields = ['transaction_amount', 'created_at']

    def get_queryset(self):
        # Ensure only transactions related to the logged-in user's beneficiaries are returned
        return Transaction.objects.filter(beneficiary__user=self.request.user)
