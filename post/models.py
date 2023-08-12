from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile, EditorProfile


#게시물 제목 tts 파일
class TTSAudioTitle(models.Model):
    title_message = models.TextField()
    audio_file = models.FileField(upload_to='tts_title/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 모델 연결

    def __str__(self):
        return self.title_message

#게시물 tts 파일
class TTSAudio(models.Model):
    message = models.TextField()
    audio_file = models.FileField(upload_to='tts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 모델 연결

    def __str__(self):
        return self.message

class Post(models.Model):
    # ID = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_nickname')
    like = models.ManyToManyField(User, related_name='liked_post', blank=True, default=0)
    published_date = models.DateTimeField(default=timezone.now)
    tts_title_audio = models.ForeignKey(TTSAudioTitle, on_delete=models.SET_NULL, null=True, blank=True)
    tts_audio = models.ForeignKey(TTSAudio, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title


class Editor_Post(models.Model):
    # ID = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor_name')
    date = models.DateField(blank=False, null=False)
    recruit_date = models.DateField(blank=False, null=False)
    place = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    like = models.ManyToManyField(User, related_name='editor_liked_post', blank=True,default=0)
    scarp = models.ManyToManyField(User, related_name='scarped_post', blank=True, default=0)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title