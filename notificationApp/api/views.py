from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from notificationApp.models import Topic, Notification, UserNotification
from .serializers import TopicSerializer, NotificationSerializer, UserNotificationSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.none()  # Provide a default empty queryset
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'is_new', 'topic__name', 'is_common']
    search_fields = ['title', 'description', 'topic__name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Get common notifications
            common_notifications = Notification.objects.filter(is_common=True)
            # Get user-specific notifications
            user_notifications = UserNotification.objects.filter(user=self.request.user).values_list('notification', flat=True)
            user_notifications = Notification.objects.filter(id__in=user_notifications)
            # Combine both
            return common_notifications | user_notifications
        return Notification.objects.none()  # Return an empty queryset if the user is not authenticated

class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.none()  # Provide a default empty queryset
    serializer_class = UserNotificationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['viewed', 'created_at', 'notification__status', 'notification__topic__name']
    search_fields = ['notification__title', 'notification__description', 'notification__topic__name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserNotification.objects.filter(user=self.request.user)
        return UserNotification.objects.none()  # Return an empty queryset if the user is not authenticated
