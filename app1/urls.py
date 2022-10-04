from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('', home, name='home_page'),
    path('about', about, name='about_page'),
    path('contacts', contacts, name='contact_page'),
]
