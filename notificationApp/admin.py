from django.contrib import admin
from .models import Topic, Notification, UserNotification

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'status', 'created_at', 'is_common')
    search_fields = ('title', 'description', 'status')
    list_filter = ('topic', 'status', 'is_common', 'created_at')

@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification', 'viewed', 'created_at')
    search_fields = ('user__username', 'notification__title')
    list_filter = ('viewed', 'created_at')

