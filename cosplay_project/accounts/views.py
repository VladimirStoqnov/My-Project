from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from cosplay_project.accounts.forms import UserCreateForm, EventForm, UserDetailsForm
from cosplay_project.accounts.models import Event, AppUser
from cosplay_project.photo.models import Photo

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'common/login.html'


class SignUpView(views.CreateView):
    template_name = 'profile/profile-register.html'
    form_class = UserCreateForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('sign in')


def user_details(request, pk):
    user = AppUser.objects.filter(pk=pk).get()
    fullname = request.user.get_full_name()
    photos = Photo.objects.all()

    user_photos = [photo for photo in photos if photo.user_id == user.pk]

    context = {
        'user': user,
        'fullname': fullname,
        'is_owner': user == request.user,
        'user_photos': user_photos

    }

    return render(request, 'profile/profile-details.html', context)


class UserEditView(views.UpdateView):
    template_name = 'profile/profile-edit.html'
    fields = ('first_name', 'last_name', 'age', 'description', )
    model = UserModel

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.object.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


def index(request):
    all_photos = Photo.objects.all()
    all_events = Event.objects.all()

    context = {
        'all_photos': all_photos,
        'all_events': all_events,
    }

    return render(request, 'common/home.html', context)


class EventCreateView(views.CreateView):
    template_name = 'event/add-event.html'
    success_url = '/'
    form_class = EventForm


class EventEditView(views.UpdateView):
    template_name = 'event/edit-event.html'
    fields = ('title', 'date_of_event', 'url')
    model = Event
    success_url = '/'


class EventDeleteView(views.DeleteView):
    template_name = 'event/delete-event.html'
    model = Event
    success_url = reverse_lazy('index')
