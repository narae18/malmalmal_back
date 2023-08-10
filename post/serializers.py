from rest_framework import serializers
from users.serializers import ProfileSerializer, EditorProfileSerializer
from .models import Post, Editor_Post, User, Profile, EditorProfile


class PostSerializer(serializers.ModelSerializer):
    nickname = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'published_date', 'like', 'nickname', 'title', 'content', 'image')
        read_only_fields = ('id', 'published_date', 'like', 'nickname')
        
        

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        

class EditorPostSerializer(serializers.ModelSerializer):
    name = EditorProfileSerializer(read_only=True)
    class Meta:
        model = Editor_Post
        fields = ('id', 'published_date', 'like', 'scarp', 'name', 'title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
        read_only_fields = ('id', 'published_date', 'like', 'scarp', 'name', 'image')


class EditorPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor_Post
        fields = ('title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
    
