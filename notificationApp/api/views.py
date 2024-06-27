from rest_framework import viewsets, permissions, status, views
from .serializers import *
from invoiceApp.models import Invoice
from rest_framework.response import Response

class NotificationViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "message_title": "title",
            "type" : "General",
            "message": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate libero et velit interdum, ac aliquet odio mattis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur tempus urna at turpis condimentum lobortis.  Curabitur tempus urna at turpis condimentum lobortis. Curabitur tempus urna at turpis condimentum lobortis."
        }
        serializer = NotificationSerializer(data)
        return Response(serializer.data)