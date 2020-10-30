"""
Created bt tz on 2020/10/27 
"""

__author__ = 'tz'

from django.urls import path
from test_app import views

urlpatterns = [
    path('users/',views.UserView.as_view()),
    path('users/<str:id>/',views.UserView.as_view())
]