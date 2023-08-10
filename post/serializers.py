from rest_framework import serializers
from users.serializers import ProfileSerializer, EditorProfileSerializer
from .models import Post, Editor_Post, User, Profile, EditorProfile


class PostSerializer(serializers.ModelSerializer):
    nickname = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('published_date', 'like', 'author', 'title', 'content')
        read_only_fields = ('id', 'published_date', 'like', 'author')
        
        

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')
        

class EditorPostSerializer(serializers.ModelSerializer):
    name = EditorProfileSerializer(read_only=True)
    class Meta:
        model = Editor_Post
        fields = ('published_date', 'like', 'scarp', 'author', 'title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
        read_only_fields = ('id','published_date', 'like', 'scarp', 'name', 'image','author')


class EditorPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor_Post
        fields = ('title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
    
