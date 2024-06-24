from rest_framework import serializers

class ReportMonthlyReportSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    sent_from = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    account_type = serializers.CharField(read_only=True)
    transaction_id = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.IntegerField(read_only=True)