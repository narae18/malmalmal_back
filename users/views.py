from rest_framework import generics
from rest_framework.generics import ListAPIView
from .serializers import  ProfileSerializer, EditorProfileSerializer
from .models import Profile, EditorProfile
from post.models import Post
from post.serializers import PostSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class UserPostsListView(ListAPIView): #로그인한 유저가 작성한 게시물 모아보기
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    
class EditorProfileView(generics.GenericAPIView):
    queryset  = EditorProfile.objects.all()
    serializer_class = EditorProfileSerializer