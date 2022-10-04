from django.urls import path

from user.views import home_user

urlpatterns = [
    path('',home_user, name='home_user'),
]