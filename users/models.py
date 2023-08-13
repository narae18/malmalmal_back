from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class EditorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor_profile')
    name = models.CharField(max_length=10, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_editor_profile(sender, instance, created, **kwargs):
    if created:
        EditorProfile.objects.create(user=instance)