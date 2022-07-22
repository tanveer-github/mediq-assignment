from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models

from api.v1.common.models import TimeStampedModel


class GenderEnum(Enum):
    """
    Enum for Genders
    """
    Male = "M"
    Female = "F"
    NonBinary = "NB"
    UniSex = "U"

    @classmethod
    def all(cls):
        return [(g.value, g.name) for g in cls]


class User(AbstractUser, TimeStampedModel):
    """
    user and profile details
    """
    gender = models.CharField(max_length=5, choices=GenderEnum.all(), default=GenderEnum.Male.value)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
