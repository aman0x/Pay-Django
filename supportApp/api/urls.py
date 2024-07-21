# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactSubmissionView, SupportInfoView, FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('contact/', ContactSubmissionView.as_view(), name='contact-submission'),
    path('support-info/', SupportInfoView.as_view(), name='support-info'),
    path('', include(router.urls)), 
]
