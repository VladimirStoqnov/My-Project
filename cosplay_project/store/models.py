from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

from cosplay_project.core.model_mixins import ChoicesEnumMixin

UserModel = get_user_model()


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

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.user} added {self.item_name} in Store on {self.publication_date}'
