# manager
from django.db import models


class JourneyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()#.filter(is_active=True).order_by('-created')
    
    def retrieve(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related('journey_steps')
        qs = qs.annotate(total_steps=models.Count('journey_steps'))
        qs = qs.annotate(total_completed_steps=models.Count('journey_steps', filter=models.Q(journey_steps__is_completed=True)))
        qs = qs.annotate(total_incomplete_steps=models.Count('journey_steps', filter=models.Q(journey_steps__is_completed=False)))
        qs = qs.annotate(total_completed_steps_percentage=models.Case(
            models.When(total_steps=0, then=0),
            default=models.F('total_completed_steps') / models.F('total_steps') * 100,
            output_field=models.FloatField()
        ))
        qs = qs.annotate(total_incomplete_steps_percentage=models.Case(
          models.When(total_steps=0, then=0),
            default=models.F('total_incompleted_steps') / models.F('total_steps') * 100,
            output_field=models.FloatField()
        ))  
        return qs
    
    def list(self):
        qs = super().get_queryset()
        qs = qs.annotate(total_steps=models.Count('journey_steps'))
        qs = qs.annotate(total_completed_steps=models.Count('journey_steps', filter=models.Q(journey_steps__is_completed=True)))    
        qs = qs.annotate(total_incomplete_steps=models.Count('journey_steps', filter=models.Q(journey_steps__is_completed=False)))
        return qs

    # def get_goals(self):


     