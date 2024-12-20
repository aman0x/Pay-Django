from rest_framework import serializers

class StatisticTransactionDashboardSerializer(serializers.Serializer):
    card_number = serializers.CharField(read_only=True)
    incomes = serializers.FloatField(read_only=True)
    expenses = serializers.FloatField(read_only=True)
    total_transactions = serializers.IntegerField(read_only=True)
    today_transactions = serializers.IntegerField(read_only=True)
    succeeded = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    total_incomes = serializers.FloatField(read_only=True)
    today_incomes = serializers.FloatField(read_only=True)
    total_payments = serializers.FloatField(read_only=True)
    today_payments = serializers.FloatField(read_only=True)
    total_successful_invoices = serializers.IntegerField(read_only=True)
    total_recieved_amount = serializers.FloatField(read_only=True)
    total_paid_tax = serializers.FloatField(read_only=True)
    monthly_income = serializers.DictField(child=serializers.IntegerField())
    monthly_expenses = serializers.DictField(child=serializers.IntegerField())
    
class StatisticInvoiceSentDashboardSerializer(serializers.Serializer):
    card_number = serializers.CharField(read_only=True)
    incomes = serializers.FloatField(read_only=True)
    total_sent_invoices = serializers.IntegerField(read_only=True)
    today_sent_invoices = serializers.IntegerField(read_only=True)
    succeeded = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    total_succeeded = serializers.FloatField(read_only=True)
    today_succeeded = serializers.FloatField(read_only=True)
    total_in_progress = serializers.FloatField(read_only=True)
    today_in_progress = serializers.FloatField(read_only=True)
    total_failed = serializers.FloatField(read_only=True)
    today_failed = serializers.FloatField(read_only=True)
    total_successful_invoices = serializers.IntegerField(read_only=True)
    total_recieved_amount = serializers.FloatField(read_only=True)
    total_paid_tax = serializers.FloatField(read_only=True)
    monthly_invoice_sent = serializers.DictField(child=serializers.IntegerField())
    
class StatisticInvoiceReceivedDashboardSerializer(serializers.Serializer):
    card_number = serializers.CharField(read_only=True)
    incomes = serializers.FloatField(read_only=True)
    total_received_invoices = serializers.IntegerField(read_only=True)
    today_received_invoices = serializers.IntegerField(read_only=True)
    succeeded = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    total_paid = serializers.FloatField(read_only=True)
    today_paid = serializers.FloatField(read_only=True)
    total_in_progress = serializers.FloatField(read_only=True)
    today_in_progress = serializers.FloatField(read_only=True)
    total_failed = serializers.FloatField(read_only=True)
    today_failed = serializers.FloatField(read_only=True)
    total_successful_invoices = serializers.IntegerField(read_only=True)
    total_paid_amount = serializers.FloatField(read_only=True)
    total_paid_tax = serializers.FloatField(read_only=True)
    monthly_invoice_received = serializers.DictField(child=serializers.IntegerField())
    
class StatisticTransactionListSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    customer = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.FloatField(read_only=True)
    commission = serializers.FloatField(read_only=True)
    
class StatisticInvoiceSentListSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    sent_to = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.FloatField(read_only=True)
    commission = serializers.FloatField(read_only=True)
    
class StatisticInvoiceReceivedListSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    sent_from = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.FloatField(read_only=True)
    commission = serializers.FloatField(read_only=True)