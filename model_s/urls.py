"""
Created bt tz on 2020/10/29 
"""

__author__ = 'tz'


from django.urls import path
from model_s import views

urlpatterns = [
    path("books/", views.BookAPIView.as_view()),
    path("books/<str:id>/", views.BookAPIView.as_view()),
    path("user/", views.UserViewSetView.as_view({"post": "user_regist","get": "user_login"})),
]