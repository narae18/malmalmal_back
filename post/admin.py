from django.contrib import admin

from .models import Post, TTSAudio

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(TTSAudio)