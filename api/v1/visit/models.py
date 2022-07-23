import datetime

from django.db import models

from api.v1.patient.models import Patient


class Visit(models.Model):
    visit_reason = models.TextField(max_length=255, null=True, blank=True)
    visit_date = models.DateTimeField(default=datetime.datetime.now())
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="visits")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'visit'

    def __str__(self):
        return self.visit_reason
