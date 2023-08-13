import os

from rest_framework import viewsets

from users.models import Profile, EditorProfile
from .models import Post, Editor_Post, TTSAudioTitle, TTSAudio, Like
# from .permissions import CustomReadOnly
from .serializers import PostSerializer, EditorPostSerializer, EditorPostCreateSerializer, TTSAudioSerializer, TTSAudioTitleSerializer

#tts 관련
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from gtts import gTTS
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostSerializer
        return PostSerializer
    
    @action(detail=False, methods=['post'])
    def create_post_with_audio(self, request):
        post_serializer = PostSerializer(data=request.data, context={'request': request})
        if post_serializer.is_valid():
            tts_title_message = request.data.get('tts_title_message')
            tts_message = request.data.get('tts_message')

            existing_tts_title = None
            existing_tts_audio = None

            if tts_title_message:
                try:
                    existing_tts_title = TTSAudioTitle.objects.get(title_message=tts_title_message, user=request.user)
                except TTSAudioTitle.DoesNotExist:
                    pass

            if tts_message:
                try:
                    existing_tts_audio = TTSAudio.objects.get(message=tts_message, user=request.user)
                except TTSAudio.DoesNotExist:
                    pass

            post = post_serializer.save(author=request.user)

            if existing_tts_title:
                post.tts_title_audio = existing_tts_title
            if existing_tts_audio:
                post.tts_audio = existing_tts_audio
            
            post.save()

            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)
    
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({'message': '좋아요 취소됨'})
        except Like.DoesNotExist:
            Like.objects.create(user=user, post=post)
            return Response({'message': '좋아요 추가됨'})
    
    
        
                
class EditorPostViewSet(viewsets.ModelViewSet):
    queryset = Editor_Post.objects.all()
    permission_classes = []
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EditorPostSerializer
        return EditorPostCreateSerializer
    
    def perform_create(self, serializer):
        editor_profile = EditorProfile.objects.get(user=self.request.user)  
        serializer.save(author=self.request.user, editor_profile=editor_profile)
        