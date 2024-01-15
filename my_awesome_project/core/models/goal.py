from django.db import models
from model_utils.models import TimeStampedModel

from .journey import Journey



class Goal(TimeStampedModel):
    name = models.CharField(max_length=255)

    journey = models.ForeignKey(
        Journey, 
        on_delete=models.CASCADE,
        related_name='goals'
        )
    

    def __str__(self):
        return self.name