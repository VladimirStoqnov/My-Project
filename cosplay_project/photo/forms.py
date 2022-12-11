from django import forms

from cosplay_project.photo.models import PhotoSession, Photo


class DateInput(forms.DateInput):
    input_type = 'date'


class PhotoSessionForm(forms.ModelForm):
    class Meta:
        model = PhotoSession
        fields = ('reserved_date', 'description')

        widgets = {
            'reserved_date': DateInput(),
        }


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    pass
