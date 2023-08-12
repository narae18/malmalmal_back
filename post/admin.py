from django.contrib import admin

from .models import Post, TTSAudio, TTSAudioTitle

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass

@admin.register(TTSAudioTitle)
class PostModelAdmin(admin.ModelAdmin):
    pass

@admin.register(TTSAudio)
class PostModelAdmin(admin.ModelAdmin):
    pass
