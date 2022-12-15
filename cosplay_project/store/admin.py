from django.contrib import admin

from cosplay_project.store.models import Items


@admin.register(Items)
class StoreAdmin(admin.ModelAdmin):
    pass
