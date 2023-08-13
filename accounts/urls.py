from django.urls import path, include
from rest_framework import routers
from .views import RegisterView, LoginView
from django.urls import path

app_name = "accounts"

# default_router = routers.SimpleRouter()
# default_router.register("register", RegisterView, basename="register")


# urlpatterns = [
#     path("", include(default_router.urls)),
# ]

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]
