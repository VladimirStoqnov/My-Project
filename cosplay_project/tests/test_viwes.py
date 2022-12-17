from django.test import SimpleTestCase
from django.urls import reverse, resolve

from cosplay_project.store.views import add_item, EditStoreItem, DeleteStoreItem, StoreHomeView
from cosplay_project.photo.views import add_photo, add_photo_sessions, DeletePhotoView, DetailsPhotoView
from cosplay_project.accounts.views import index, SignInView, SignUpView, SignOutView, UserEditView, \
    UserDeleteView, EventCreateView, EventEditView, EventDeleteView, user_details


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_user_edit_url_is_resolved(self):
        url = reverse('edit user', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserEditView)

    def test_user_details_url_is_resolved(self):
        url = reverse('details user', args=[1])
        self.assertEquals(resolve(url).func, user_details)

    def test_user_delete_url_is_resolved(self):
        url = reverse('delete user', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)

    def test_sign_in_url_is_resolved(self):
        url = reverse('sign in')
        self.assertEquals(resolve(url).func.view_class, SignInView)

    def test_sign_up_url_is_resolved(self):
        url = reverse('sign up')
        self.assertEquals(resolve(url).func.view_class, SignUpView)

    def test_sign_out_url_is_resolved(self):
        url = reverse('logout user')
        self.assertEquals(resolve(url).func.view_class, SignOutView)

    def test_event_create_url_is_resolved(self):
        url = reverse('create event')
        self.assertEquals(resolve(url).func.view_class, EventCreateView)

    def test_event_edit_url_is_resolved(self):
        url = reverse('edit event', args=[1])
        self.assertEquals(resolve(url).func.view_class, EventEditView)

    def test_event_delete_url_is_resolved(self):
        url = reverse('delete event', args=[1])
        self.assertEquals(resolve(url).func.view_class, EventDeleteView)

    def test_add_photo_url_is_resolved(self):
        url = reverse('add photo')
        self.assertEquals(resolve(url).func, add_photo)

    def test_add_photo_session_url_is_resolved(self):
        url = reverse('photo session')
        self.assertEquals(resolve(url).func, add_photo_sessions)

    def test_store_add_item_session_url_is_resolved(self):
        url = reverse('add item')
        self.assertEquals(resolve(url).func, add_item)

    def test_store_home_url_is_resolved(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func.view_class, StoreHomeView)

    def test_store_edit_item_url_is_resolved(self):
        url = reverse('edit item', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditStoreItem)

    def test_store_delete_item_url_is_resolved(self):
        url = reverse('delete item', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteStoreItem)
