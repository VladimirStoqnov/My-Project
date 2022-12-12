from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from cosplay_project.accounts.models import Event

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        field_classes = {"username": auth_forms.UsernameField}


class UserCreateForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'age')
        fields_class = {'username': auth_forms.UsernameField}


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date_of_event': DateInput(),
        }

