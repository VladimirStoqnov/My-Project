from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Photo(models.Model):

    str_fields = ('photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='user_photos/',
        null=False,
        blank=True,
    )

    description = models.CharField(

        max_length=MAX_DESCRIPTION_LENGTH,
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=False,
        blank=False,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class PhotoSession(models.Model):

    reserved_date = models.DateField(
        unique=True,
    )
    description = models.TextField(max_length=200,)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

