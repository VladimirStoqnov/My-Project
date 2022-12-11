from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from cosplay_project.accounts.forms import UserCreateForm, EventForm
from cosplay_project.accounts.models import Event
from cosplay_project.photo.models import Photo

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'login.html'


class SignUpView(views.CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('sign in')


class UserDetailsView(views.DetailView):
    template_name = 'profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        return context


class UserEditView(views.UpdateView):
    template_name = 'edit.html'
    fields = ('first_name', 'last_name', 'age', 'description', )
    model = UserModel

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.object.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


def index(request):
    all_photos = Photo.objects.all()
    all_events = Event.objects.all()

    context = {
        'all_photos': all_photos,
        'all_events': all_events,
    }

    return render(request, 'home.html', context)


class EventCreateView(views.CreateView):
    template_name = 'add-event.html'
    success_url = '/'
    form_class = EventForm


class EventEditView(views.UpdateView):
    template_name = 'edit-event.html'
    fields = ('title', 'date_of_event', 'url')
    model = Event
    success_url = '/'


class EventDeleteView(views.DeleteView):
    template_name = 'delete-event.html'
    model = Event
    success_url = reverse_lazy('index')
