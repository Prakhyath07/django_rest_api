from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth_token'),

    path('', views.api_home, name='api-home')
]