from django.urls import path

from cosplay_project.photo.views import add_photo, add_photo_sessions, DeletePhotoView

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('photosession/', add_photo_sessions, name='photo session'),
    path('photo/<int:pk>/', DeletePhotoView.as_view(), name='delete photo'),

)