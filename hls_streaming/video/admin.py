from django.contrib import admin
from .models import Video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ['created_at','updated_at', 'name', 'slug', 'description', 'video', 'thumbnail', 'duration', 'hls', 'status', 'is_running']
admin.site.register(Video, VideoAdmin)