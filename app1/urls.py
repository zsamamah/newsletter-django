from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('', home, name='home_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page'),
]
