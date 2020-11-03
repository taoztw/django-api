"""
Created bt tz on 2020/11/3 
"""

__author__ = 'tz'

from django.urls import path

from api import views

urlpatterns = [
    path("demo/", views.Demo.as_view()),
    path("user/", views.UserAPIView.as_view()),
]