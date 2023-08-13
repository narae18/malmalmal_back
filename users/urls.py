from django.urls import path
from .views import RegisterView, LoginView, ProfileListView, ProfileView, EditorProfileView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileListView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('editorprofile/<int:pk>/', EditorProfileView.as_view()),
]
