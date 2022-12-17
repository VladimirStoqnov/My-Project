from django.contrib import admin

from cosplay_project.store.models import Items


@admin.register(Items)
class StoreAdmin(admin.ModelAdmin):
    ordering = ['item_name', ]
    list_display = ['item_name', 'type', 'user']
    list_filter = ['item_name', 'type', 'user']
