"""
Created bt tz on 2020/10/28 
"""

__author__ = 'tz'

from django.urls import path
from seria import views


urlpatterns = [
    path('teachers/',views.TercherView.as_view()),
    path('teachers/<str:id>/',views.TercherView.as_view())
]