from django.urls import path, include

from cosplay_project.accounts.views import index, SignInView, SignUpView, SignOutView, UserEditView, \
    UserDeleteView, EventCreateView, EventEditView, EventDeleteView, user_details

urlpatterns = (
    path('', index, name='index'),
    path('login/', SignInView.as_view(), name='sign in'),
    path('register/', SignUpView.as_view(), name='sign up'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', user_details, name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
    path('add/', EventCreateView.as_view(), name='create event'),
    path('event/<int:pk>', include([
        path('edit/', EventEditView.as_view(), name='edit event'),
        path('delete/', EventDeleteView.as_view(), name='delete event'),
    ])),
)
