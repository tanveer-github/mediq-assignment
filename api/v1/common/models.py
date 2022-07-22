from django.db import models


class TimeStampedModel(models.Model):
    """
    Base model for all models for which we need created_at & updated_at fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class to make model abstract
        """
        abstract = True
