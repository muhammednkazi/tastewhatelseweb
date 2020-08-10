from django.contrib import admin
from .models import video,videoComment
# Register your models here.

admin.site.register(videoComment)

# registering video model by using decorator
# because we want to customize admin page of the video model
# we will be using tinymce editor for writing content of video.
@admin.register(video)
class videoAdmin(admin.ModelAdmin):
    class Media:
        js=('tinymceinject.js',) #this file is stored in static folder