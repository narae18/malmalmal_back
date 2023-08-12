from rest_framework import serializers
from users.serializers import ProfileSerializer, EditorProfileSerializer
from .models import Post, Editor_Post, User, Profile, EditorProfile, TTSAudio, TTSAudioTitle
from gtts import gTTS
from django.conf import settings
import os

class TTSAudioTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTSAudioTitle
        fields = '__all__'
        
class TTSAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTSAudio
        fields = '__all__'
          

class PostSerializer(serializers.ModelSerializer):
    nickname = ProfileSerializer(read_only=True)
    tts_title_message = serializers.CharField(max_length=100, required=False)
    tts_message = serializers.CharField(max_length=1000, required=False)
    
    class Meta:
        model = Post
        fields = ('published_date', 'like', 'author', 'title', 'content', 'nickname', 'tts_title_message', 'tts_message')
        read_only_fields = ('id', 'published_date', 'like', 'author', 'nickname')
    
    def create(self, validated_data):
        tts_title_message = validated_data.pop('tts_title_message', None)
        tts_message = validated_data.pop('tts_message', None)
        
        author = self.context['request'].user
        
        post = Post.objects.create(**validated_data)

        if tts_title_message: 
            tts_title = gTTS(text=tts_title_message, lang='ko')
            tts_title_audio = TTSAudioTitle(title_message=tts_title_message, user=author)
            tts_title_audio.save()

            tts_folder = os.path.join(settings.MEDIA_ROOT, 'tts_title')
            os.makedirs(tts_folder, exist_ok=True)

            save_path = os.path.join(tts_folder, f'tts_title_{tts_title_audio.id}.mp3')
            tts_title.save(save_path)

            tts_title_audio.audio_file = f'tts_title/tts_title_{tts_title_audio.id}.mp3'
            tts_title_audio.save()

            post.tts_title_audio = tts_title_audio
            
        if tts_message:
            tts = gTTS(text=tts_message, lang='ko')
            tts_audio = TTSAudio(message=tts_message, user=author)
            tts_audio.save()

            tts_folder = os.path.join(settings.MEDIA_ROOT, 'tts')
            os.makedirs(tts_folder, exist_ok=True)

            save_path = os.path.join(tts_folder, f'tts_{tts_audio.id}.mp3')
            tts.save(save_path)

            tts_audio.audio_file = f'tts/tts_{tts_audio.id}.mp3'
            tts_audio.save()

            post.tts_audio = tts_audio

        post.save()

        return post
        

# class PostCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('title', 'content')
        

class EditorPostSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='name.user', read_only=True)

    class Meta:
        model = Editor_Post
        fields = ('name', 'published_date', 'like', 'scarp', 'author', 'title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
        read_only_fields = ('id', 'published_date', 'like', 'scarp', 'name', 'image', 'author')



class EditorPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor_Post
        fields = ('title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
    
