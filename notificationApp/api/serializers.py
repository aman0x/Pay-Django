from rest_framework import serializers
from notificationApp.models import Topic, Notification, UserNotification

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']  # Specify the fields you want to return

class NotificationSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = '__all__'

class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = '__all__'