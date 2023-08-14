from django.urls import path
# from rest_framework import routers
from .views import RegisterView, LoginView, ProfileView

app_name = "accounts"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
