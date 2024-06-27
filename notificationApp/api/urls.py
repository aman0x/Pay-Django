from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('data/', views.NotificationViewSet.as_view(), name="notification"),
]
