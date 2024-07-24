from rest_framework import serializers
from transactionApp.models import Transaction, Beneficiary
from invoiceApp.models import Service
from userApp.models import BankAccount
from cardApp.models import Card

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        ref_name = 'TransactionService'
        fields = ['id', 'name', 'description', 'price']

class BeneficiaryBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['account_name', 'account_number', 'ifsc_code', 'bank_name']

class BeneficiarySerializer(serializers.ModelSerializer):
    bank_account = BeneficiaryBankAccountSerializer()

    class Meta:
        model = Beneficiary
        fields = ['id', 'name', 'phone_number', 'bank_account', 'verified', 'verified_at']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        ref_name = 'TransactionCard'
        fields = ['id', 'card_no', 'expiry_date', 'card_holder_name']

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        ref_name = 'TransactionBankAccount'
        fields = ['id', 'account_name', 'account_number', 'ifsc_code', 'bank_name']

class TransactionSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, write_only=True)
    beneficiary = serializers.PrimaryKeyRelatedField(queryset=Beneficiary.objects.all())
    card_id = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), write_only=True, required=False, allow_null=True)
    bank_account_id = serializers.PrimaryKeyRelatedField(queryset=BankAccount.objects.all(), write_only=True, required=False, allow_null=True)
    card = CardSerializer(read_only=True)
    bank_account = BankAccountSerializer(read_only=True)
    beneficiary_name = serializers.CharField(source='beneficiary.name', read_only=True)
    transaction_number = serializers.CharField(read_only=True)
    transaction_status = serializers.CharField(read_only=True)
    beneficiary_bank_account = BeneficiaryBankAccountSerializer(source='beneficiary.bank_account', read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_number', 'transaction_amount', 'transaction_status', 'beneficiary', 'beneficiary_name', 
            'services', 'service_ids', 'transaction_type', 'card_id', 'bank_account_id', 'card', 'bank_account', 
            'created_at', 'beneficiary_bank_account'
        ]

    def create(self, validated_data):
        service_ids = validated_data.pop('service_ids')
        card_id = validated_data.pop('card_id', None)
        bank_account_id = validated_data.pop('bank_account_id', None)

        if validated_data['transaction_type'] == 'card':
            if card_id is None:
                raise serializers.ValidationError("Card ID must be provided for card transactions.")
            validated_data['card'] = card_id
        elif validated_data['transaction_type'] == 'bank':
            if bank_account_id is None:
                raise serializers.ValidationError("Bank account ID must be provided for bank transactions.")
            validated_data['bank_account'] = bank_account_id

        transaction = Transaction.objects.create(**validated_data)
        transaction.services.set(service_ids)
        return transaction

    def update(self, instance, validated_data):
        service_ids = validated_data.pop('service_ids', None)
        card_id = validated_data.pop('card_id', None)
        bank_account_id = validated_data.pop('bank_account_id', None)

        if validated_data['transaction_type'] == 'card':
            if card_id is None:
                raise serializers.ValidationError("Card ID must be provided for card transactions.")
            instance.card = card_id
            instance.bank_account = None
        elif validated_data['transaction_type'] == 'bank':
            if bank_account_id is None:
                raise serializers.ValidationError("Bank account ID must be provided for bank transactions.")
            instance.bank_account = bank_account_id
            instance.card = None

        if service_ids is not None:
            instance.services.set(service_ids)

        return super().update(instance, validated_data)
