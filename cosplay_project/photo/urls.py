from django.urls import path, include

from cosplay_project.photo.views import add_photo, add_photo_sessions, DeletePhotoView, DetailsPhotoView

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('photosession/', add_photo_sessions, name='photo session'),
    path('photo/<int:pk>/', include([
        path('', DetailsPhotoView.as_view(),  name='details photo'),
        path('delete/', DeletePhotoView.as_view(), name='delete photo')
    ])),


)