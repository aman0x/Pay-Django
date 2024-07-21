from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from notificationApp.models import Topic, Notification, UserNotification
from .serializers import TopicSerializer, NotificationSerializer, UserNotificationSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get common notifications
        common_notifications = Notification.objects.filter(is_common=True)
        # Get user-specific notifications
        user_notifications = UserNotification.objects.filter(user=self.request.user).values_list('notification', flat=True)
        user_notifications = Notification.objects.filter(id__in=user_notifications)
        # Combine both
        return common_notifications | user_notifications

class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserNotification.objects.filter(user=self.request.user)