from rest_framework import viewsets, permissions, status
from .serializers import CardSerializer
from cardApp.models import Card

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]