from rest_framework import serializers
from transactionApp.models import Transaction
from invoiceApp.models import Service
from userApp.models import BankAccount
from cardApp.models import Card
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        ref_name = 'InvoiceService'
        fields = ['id', 'name', 'description', 'price']

class TransactionSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, write_only=True)
    receivable_name = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    card_id = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), write_only=True, required=False, allow_null=True)
    bank_account_id = serializers.PrimaryKeyRelatedField(queryset=BankAccount.objects.all(), write_only=True, required=False, allow_null=True)
    card = serializers.StringRelatedField(read_only=True)
    bank_account = serializers.StringRelatedField(read_only=True)
    receivable_name_username = serializers.CharField(source='receivable_name.username', read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_amount', 'receivable_name', 'receivable_name_username', 'services', 'service_ids', 
            'transaction_type', 'card_id', 'bank_account_id', 'card', 'bank_account', 'created_at'
        ]

    def create(self, validated_data):
        service_ids = validated_data.pop('service_ids')
        card_id = validated_data.pop('card_id', None)
        bank_account_id = validated_data.pop('bank_account_id', None)

        if validated_data['transaction_type'] == 'card' and card_id:
            validated_data['card'] = card_id
        elif validated_data['transaction_type'] == 'bank' and bank_account_id:
            validated_data['bank_account'] = bank_account_id

        transaction = Transaction.objects.create(**validated_data)
        transaction.services.set(service_ids)
        return transaction

    def update(self, instance, validated_data):
        service_ids = validated_data.pop('service_ids', None)
        card_id = validated_data.pop('card_id', None)
        bank_account_id = validated_data.pop('bank_account_id', None)

        if validated_data['transaction_type'] == 'card' and card_id:
            instance.card = card_id
        elif validated_data['transaction_type'] == 'bank' and bank_account_id:
            instance.bank_account = bank_account_id

        if service_ids is not None:
            instance.services.set(service_ids)

        return super().update(instance, validated_data)
