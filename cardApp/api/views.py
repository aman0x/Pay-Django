from rest_framework import viewsets, permissions, status
from .serializers import CardSerializer
from cardApp.models import Card
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

