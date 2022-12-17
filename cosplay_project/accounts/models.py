from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from cosplay_project.core.validators import validate_only_letters, validate_only_letters_and_spaces


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 5
    MAX_LENGTH_FIRST_NAME = 25
    MIN_LENGTH_USERNAME = 5
    MAX_LENGTH_USERNAME = 20
    MIN_LENGTH_LAST_NAME = 5
    MAX_LENGTH_LAST_NAME = 25
    MAX_LENGTH_DESCRIPTION = 100

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME, 'First Name must have at least 5 letters!'),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME, 'Last Name must have at least 5 letters!'),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    username = models.CharField(
        'Username',
        unique=True,
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_USERNAME, 'Username must have at least 5 letters!'),
            validate_only_letters,
        )
    )

    description = models.TextField(
        max_length=MAX_LENGTH_DESCRIPTION,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class Event(models.Model):
    TITLE_MIN_LENGTH = 5
    TITLE_MAX_LENGTH = 50
    URL_MIN_LENGTH = 5
    URL_MAX_LENGTH = 200

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(TITLE_MIN_LENGTH, f'Please add at least {TITLE_MIN_LENGTH} letters'),
            validate_only_letters_and_spaces,
        )
    )

    date_of_event = models.DateField()
    url = models.URLField(
        max_length=URL_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(URL_MIN_LENGTH, f'Please add at least {URL_MIN_LENGTH} letters'),
        )
    )

    def __str__(self):
        return f'{self.title} is added with date {self.date_of_event}'
