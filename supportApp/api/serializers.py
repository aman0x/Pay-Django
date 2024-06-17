from rest_framework import serializers
from supportApp.models import Support

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Support
        fields= "__all__"