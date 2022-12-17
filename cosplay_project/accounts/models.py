from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from cosplay_project.core.validators import validate_only_letters


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 3
    MAX_LENGTH_FIRST_NAME = 25
    MIN_LENGTH_LAST_NAME = 3
    MAX_LENGTH_LAST_NAME = 25

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class Event(models.Model):

    title = models.CharField(max_length=50,)
    date_of_event = models.DateField()
    url = models.URLField(max_length=255)

    def __str__(self):
        return f'{self.title} is added with date {self.date_of_event}'
