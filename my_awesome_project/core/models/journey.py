from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Journey(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name