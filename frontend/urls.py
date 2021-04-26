from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
