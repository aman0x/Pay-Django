from rest_framework import serializers
from notificationApp.models import Topic, Notification, UserNotification

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']

class NotificationSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    topic_id = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), source='topic', write_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'title', 'description', 'data', 'status', 'is_new', 'topic', 'topic_id', 'created_at', 'is_common']

class UserNotificationSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer(read_only=True)
    notification_id = serializers.PrimaryKeyRelatedField(queryset=Notification.objects.all(), source='notification', write_only=True)

    class Meta:
        model = UserNotification
        fields = ['id', 'user', 'notification', 'notification_id', 'viewed', 'created_at']
