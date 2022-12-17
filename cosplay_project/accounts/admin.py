from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from cosplay_project.accounts.forms import UserEditForm, UserCreateForm
from cosplay_project.accounts.models import Event

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
    ordering = ['username', ]
    list_filter = ['first_name', 'last_name', 'email', 'groups']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ['title', ]
    list_display = ['title', 'date_of_event']
    list_filter = ['title', 'date_of_event']
