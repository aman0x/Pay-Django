from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CardViewSet, BinCheckView



router = DefaultRouter()
router.register(r'cards', CardViewSet, basename='card')

urlpatterns = [
    path('card-validation', include(router.urls)),
    path('check/<str:bin_code>/', BinCheckView.as_view(), name='bin_check'),
    path('', include(router.urls)),
]
