import datetime

from django.conf import settings
from django.db import models

from api.v1.common.models import TimeStampedModel
from api.v1.patient.models import Patient


class Visit(TimeStampedModel):
    visit_reason = models.TextField(max_length=100, null=True, blank=True)
    visit_date = models.DateTimeField(default=datetime.datetime.now())
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="visits")

    class Meta:
        app_label = 'visit'

    def __str__(self):
        return self.visit_reason
