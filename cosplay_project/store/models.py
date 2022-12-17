from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Type(ChoicesEnumMixin, Enum):
    weapon = 'Weapon'
    clothe = 'Clothe'
    accessories = 'Accessories'
    manga = 'Manga'


class Items(models.Model):
    ITEM_NAME_LENGTH = 30
    DESCRIPTION_LENGTH = 100

    item_name = models.CharField(
        max_length=ITEM_NAME_LENGTH,
    )

    description = models.TextField(
        max_length=DESCRIPTION_LENGTH
    )

    price = models.PositiveIntegerField()

    image = models.URLField()

    type = models.CharField(
        choices=Type.choices(),
        max_length=Type.max_len(),
    )

    publication_date = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.user} added {self.item_name} in Store on {self.publication_date}'
