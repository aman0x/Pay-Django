from rest_framework import serializers
from invoiceApp.models import Invoice, Service
from userApp.models import Beneficiary, BankAccount
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']

class BeneficiaryBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        ref_name = 'InvoiceBeneficiaryBankAccount'
        fields = ['account_name', 'account_number', 'ifsc_code', 'bank_name']

class BeneficiarySerializer(serializers.ModelSerializer):
    bank_account = BeneficiaryBankAccountSerializer(read_only=True)

    class Meta:
        model = Beneficiary
        fields = ['id', 'name', 'phone_number', 'bank_account', 'verified', 'verified_at']

class InvoiceSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    beneficiary = serializers.PrimaryKeyRelatedField(queryset=Beneficiary.objects.all())
    beneficiary_name = serializers.CharField(source='beneficiary.name', read_only=True)
    beneficiary_bank_account = BeneficiaryBankAccountSerializer(source='beneficiary.bank_account', read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, write_only=True)
    invoice_number = serializers.CharField(read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'user', 'user_id', 'beneficiary', 'beneficiary_name', 'beneficiary_bank_account', 'amount', 'tax', 'services', 'service_ids', 'created_at', 'status', 'invoice_number']

    def create(self, validated_data):
        user = validated_data.pop('user_id')
        service_ids = validated_data.pop('service_ids')
        beneficiary = validated_data.pop('beneficiary')
        
        invoice = Invoice.objects.create(user=user, beneficiary=beneficiary, **validated_data)
        invoice.services.set(service_ids)
        return invoice

    def update(self, instance, validated_data):
        service_ids = validated_data.pop('service_ids', None)
        
        if service_ids is not None:
            instance.services.set(service_ids)

        return super().update(instance, validated_data)






        
class InvoiceSentDashboardSerializer(serializers.Serializer):
    all_invoices = serializers.IntegerField(read_only=True)
    successful = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    today_successful = serializers.IntegerField(read_only=True)
    today_in_progress = serializers.IntegerField(read_only=True)
    today_failed = serializers.IntegerField(read_only=True)
    today_refunded = serializers.IntegerField(read_only=True)
    
class InvoiceReceivedDashboardSerializer(serializers.Serializer):
    all_invoices = serializers.IntegerField(read_only=True)
    successful = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    today_successful = serializers.IntegerField(read_only=True)
    today_in_progress = serializers.IntegerField(read_only=True)
    today_failed = serializers.IntegerField(read_only=True)
    today_refunded = serializers.IntegerField(read_only=True)
    
class InvoiceAllInvoiceSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    recipient = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    account_type = serializers.CharField(read_only=True)
    transaction_id = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.FloatField(read_only=True)
    
class InvoiceDetailsSerializer(serializers.Serializer):
    status = serializers.CharField(read_only=True)
    invoice_title = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    invoice_id = serializers.CharField(read_only=True)
    particulars = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    price_per_quantity = serializers.FloatField(read_only=True)
    amount = serializers.FloatField(read_only=True)
    gst = serializers.IntegerField(read_only=True)
    subtotal = serializers.FloatField(read_only=True)
    name = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    account_number = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    bank_branch = serializers.CharField(read_only=True)    
    ifsc_code = serializers.CharField(read_only=True)
    total_amount = serializers.FloatField(read_only=True)
    
class InvoiceNewInvoicesSerializer(serializers.Serializer):
    invoice_title = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    invoice_id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    bank_branch = serializers.CharField(read_only=True)    
    ifsc_code = serializers.CharField(read_only=True)
    total_amount = serializers.FloatField(read_only=True)    