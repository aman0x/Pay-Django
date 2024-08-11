"""
URL configuration for paymorz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="paymorz",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/user/', include('userApp.api.urls')),
    path('api/card/', include('cardApp.api.urls')),
    path('api/support/', include('supportApp.api.urls')),
    path('api/dashboard/', include('dashboardApp.api.urls')),
    path('api/report/', include('reportApp.api.urls')),
    path('api/payment/', include('paymentApp.api.urls')),
    path('api/invoice/', include('invoiceApp.api.urls')),
    path('api/transaction/', include('transactionApp.api.urls')),
    path('api/statistic/', include('statisticApp.api.urls')),
    path('api/notification/', include('notificationApp.api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    

]
