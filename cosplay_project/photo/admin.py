from django.contrib import admin

from cosplay_project.photo.models import Photo, PhotoSession


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ordering = ['user', ]
    list_filter = ['user', 'location', 'publication_date']
    list_display = ['user', 'location', 'publication_date',]


@admin.register(PhotoSession)
class PhotoSessionAdmin(admin.ModelAdmin):
    ordering = ['user', ]
    list_filter = ['user', 'reserved_date']
    list_display = ['user', 'reserved_date']
