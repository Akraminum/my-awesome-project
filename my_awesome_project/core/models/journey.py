from django.db import models
from model_utils.models import TimeStampedModel


class Journey(TimeStampedModel):
    name = models.CharField(max_length=255)

    # objects = JourneyManager()

    def __str__(self):
        return self.name
