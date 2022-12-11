from django.contrib import admin

from cosplay_project.photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
