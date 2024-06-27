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