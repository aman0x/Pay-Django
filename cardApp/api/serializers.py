from rest_framework import serializers
from cardApp.models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields= "__all__"