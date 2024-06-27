from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    message_title = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)