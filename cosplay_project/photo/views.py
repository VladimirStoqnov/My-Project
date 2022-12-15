from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cosplay_project.photo.forms import PhotoCreateForm, PhotoSessionForm
from cosplay_project.photo.models import Photo

UserModel = get_user_model()


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'photo/add_photo.html', context)


@login_required()
def add_photo_sessions(request):
    if request.method == 'GET':
        form = PhotoSessionForm()
    else:
        form = PhotoSessionForm(request.POST)
        if form.is_valid():
            photo_session = form.save(commit=False)
            photo_session.user = request.user
            photo_session.save()
            return redirect('index')
    context = {
        'form': form,
    }

    return render(request, 'photo_session/photo_session.html', context)


class DetailsPhotoView(views.DetailView):
    model = Photo
    queryset = Photo.objects.all()
    template_name = 'photo/details-photo.html'


class DeletePhotoView(views.DeleteView):
    template_name = 'photo/delete-photo.html'
    model = Photo

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })
