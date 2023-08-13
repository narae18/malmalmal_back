from django.urls import path
from rest_framework import routers
from .views import PostViewSet, EditorPostViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('editorposts', EditorPostViewSet)


# urlpatterns = router.urls
urlpatterns = [
    *router.urls,
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
]