from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from transactionApp.models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['transaction_amount', 'receivable_user', 'transaction_type', 'created_at', 'services']
    search_fields = ['receivable_user__username', 'services__name', 'card__card_holder_name', 'bank_account__account_name']
    ordering_fields = ['transaction_amount', 'created_at']
