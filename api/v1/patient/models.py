from datetime import date

from django.conf import settings
from django.db import models
from api.v1.common.models import TimeStampedModel


class Patient(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=date.today)

    class Meta:
        app_label = 'patient'

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
