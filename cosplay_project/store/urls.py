from django.urls import path, include

from cosplay_project.store.views import add_item, EditStoreItem, DeleteStoreItem, store

urlpatterns = (
    path('', store, name='store'),
    path('add/', add_item, name='add item'),
    path('store/<int:pk>/', include([
        path('edit/', EditStoreItem.as_view(), name='edit item'),
        path('delete/', DeleteStoreItem.as_view(), name='delete item'),
    ]))
)
