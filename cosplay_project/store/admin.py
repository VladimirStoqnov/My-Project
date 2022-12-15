from django.contrib import admin

from cosplay_project.store.models import Items

@admin.register(admin.ModelAdmin)
class StoreAdmin(Items):
    pass