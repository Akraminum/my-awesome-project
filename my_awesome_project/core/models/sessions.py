from django.db import models
from model_utils.models import TimeStampedModel

from .task import Task


class Session(TimeStampedModel):
    minutes = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    task = models.ForeignKey(
        Task,
        verbose_name="Session Task",
        related_name="sessions",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
