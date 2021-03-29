from django.contrib import admin
from django.urls import path

from .views import  contactView

urlpatterns = [
    # path('', index , name = "main"),
    path('', contactView, name='contact'),
    # path('success/', successView, name='success'),
]