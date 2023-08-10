from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile, EditorProfile

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    nickname = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='nickname')
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class Editor_Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    name = models.ForeignKey( EditorProfile, on_delete=models.CASCADE, related_name='editor_name')
    date = models.DateField(blank=False, null=False)
    recruit_date = models.DateField(blank=False, null=False)
    place = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    like = models.IntegerField(default=0)
    scrap = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title