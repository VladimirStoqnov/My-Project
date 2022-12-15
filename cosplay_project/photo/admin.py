from django.contrib import admin

from cosplay_project.photo.models import Photo, PhotoSession


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoSession)
class PhotoSessionAdmin(admin.ModelAdmin):
    pass
