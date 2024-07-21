from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, NotificationViewSet, UserNotificationViewSet

router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'user-notifications', UserNotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
