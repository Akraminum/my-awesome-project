from django.db import models
from model_utils.models import TimeStampedModel

from my_awesome_project.core.managers.JourneyManager import JourneyManager


class Journey(TimeStampedModel):
    name = models.CharField(max_length=255)

    objects = JourneyManager()

    def __str__(self):
        return self.name
