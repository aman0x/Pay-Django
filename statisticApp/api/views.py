from rest_framework import viewsets, permissions, status, views
from .serializers import *
from invoiceApp.models import Invoice
from rest_framework.response import Response

class StatisticTransactionDashboardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "card_number" : "1234567824681257",
            "incomes" : 24000.70,
            "expenses" : 24000.70,
            "total_transactions" : 1200,
            "today_transactions" : 4,
            "succeeded" : 12,
            "in_progress" : 12,
            "failed" : 12,
            "refunded" : 12,
            "total_incomes" : 24000.70,
            "today_incomes" : 1290,
            "total_payments" : 240.70,
            "today_payments" : 12,
            "total_successful_invoices" : 500,
            "total_recieved_amount" : 24000.24,
            "total_paid_tax" : 240.24
        }
        serializer = StatisticTransactionDashboardSerializer(data)
        return Response(serializer.data)