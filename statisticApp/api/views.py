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
    
class StatisticInvoiceSentDashboardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "card_number" : "1234567824681257",
            "incomes" : 24000.70,
            "total_sended_invoices" : 1200,
            "today_sended_invoices" : 4,
            "succeeded" : 12,
            "in_progress" : 12,
            "failed" : 12,
            "refunded" : 12,
            "total_succeeded" : 24000.24,
            "today_succeeded" : 1290,
            "total_in_progress" : 240.70,
            "today_in_progress" : 12,
            "total_failed" : 240.70,
            "today_failed" : 12,
            "total_successful_invoices" : 500,
            "total_recieved_amount" : 24000.24,
            "total_paid_tax" : 240.24
        }
        serializer = StatisticInvoiceSentDashboardSerializer(data)
        return Response(serializer.data)
    
class StatisticInvoiceReceivedDashboardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "card_number" : "1234567824681257",
            "incomes" : 24000.70,
            "total_received_invoices" : 1200,
            "today_received_invoices" : 4,
            "succeeded" : 12,
            "in_progress" : 12,
            "failed" : 12,
            "refunded" : 12,
            "total_paid" : 24000.24,
            "today_paid" : 1290,
            "total_in_progress" : 240.70,
            "today_in_progress" : 12,
            "total_failed" : 240.70,
            "today_failed" : 12,
            "total_successful_invoices" : 500,
            "total_paid_amount" : 24000.24,
            "total_paid_tax" : 240.24
        }
        serializer = StatisticInvoiceReceivedDashboardSerializer(data)
        return Response(serializer.data)
    
class StatisticTransactionListViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "customer": "John P.",
            "type" : "Vendor_Payment",
            "bank": "HDFC Bank , KODAD, HDFC0001642",
            "status" : "Succeeded",
            "sum": 24000.24,
            "commission" : 240.24
        }
        serializer = StatisticTransactionListSerializer(data)
        return Response(serializer.data)
    
class StatisticInvoiceSentListViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "sent_to": "John P.",
            "type" : "Vendor_Payment",
            "bank": "HDFC Bank , KODAD, HDFC0001642",
            "status" : "Succeeded",
            "sum": 24000.24,
            "commission" : 240.24
        }
        serializer = StatisticInvoiceSentListSerializer(data)
        return Response(serializer.data)
    
class StatisticInvoiceReceivedListViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "sent_from": "John P.",
            "type" : "Vendor_Payment",
            "bank": "HDFC Bank , KODAD, HDFC0001642",
            "status" : "Succeeded",
            "sum": 24000.24,
            "commission" : 240.24
        }
        serializer = StatisticInvoiceReceivedListSerializer(data)
        return Response(serializer.data)