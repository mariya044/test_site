"""
URL configuration for test_site project.

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
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from users.views import UserAPIDetailView, UserAPIView

from users.views import SignUp

app_name = "users"
urlpatterns = [
    path(
        'swagger-ui/',
        TemplateView.as_view(
            template_name='docs.html',
            extra_context={'schema_url': 'api_schema'}
        ),
        name='swagger-ui'),
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('admin/', admin.site.urls),
    path("users/", UserAPIView.as_view(
            template_name='UserView.html',
        ), name="users"),
    path("auth/", include('djoser.urls')),
    re_path(r"^auth/", include('djoser.urls.authtoken')),
    path("users/<int:id>/", UserAPIDetailView.as_view(), name="users_detail"),
    path('signup/', SignUp.as_view(), name="signup"),
]
