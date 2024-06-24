from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('quick-send/', views.DashboardQuickSendViewSet.as_view(), name="quick-send"),
    path('total-month-spendings/', views.DashboardTotalMonthSpendingsViewSet.as_view(), name="total-month-spendings"),
    path('my-template/', views.DashboardMyTemplateViewSet.as_view(), name="my-template"),
    path('my-card/', views.DashboardMyCardViewSet.as_view(), name="my-card"),
    path('stats/', views.DashboardStatsViewSet.as_view(), name="stats"),
    path('latest-actions/', views.DashboardLatestActionsViewSet.as_view(), name="latest-actions"),
]