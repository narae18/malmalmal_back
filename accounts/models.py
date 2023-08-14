from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=10, null=False, blank=False)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=False, blank=False) 
    editor_name = models.CharField(max_length=10, null=True, blank=True)
    
    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

