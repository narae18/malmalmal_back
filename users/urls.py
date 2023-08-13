from django.urls import path
from .views import ProfileListView, ProfileView, EditorProfileView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileListView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('editorprofile/<int:pk>/', EditorProfileView.as_view()),
]
