from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django.db.models import Count

from my_awesome_project.core.api.serializers.journey.create import JourneyCreateSerializer
from my_awesome_project.core.api.serializers.journey.detail import JourneyDetailSerializer
from my_awesome_project.core.api.serializers.journey.list import JourneyListSerializer
from my_awesome_project.core.api.serializers.journey.update import JourneyUpdateSerializer

from my_awesome_project.core.models import Journey, Goal
from django.db.models import Prefetch, Q

    
class JourneyViewSet(viewsets.ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    ordering = ['name']
    
    # TODO: will be moved to model manager
    queryset_map = {
        "default": Journey.objects.all(),
        "list": Journey.objects.all().annotate(goals_count=Count('goals')),
        "retrieve": Journey.objects.all().prefetch_related(
            Prefetch(
                'goals', 
                queryset=Goal.objects.all().annotate(
                    total_targets_count=Count('targets'),
                    achieved_targets_count=Count('targets', filter=Q(targets__is_achieved=True))
                )
            )
        )
    } 
    def get_queryset(self):
        return self.queryset_map.get(
            self.action,
            self.queryset_map.get("default"))
        
    
    serializer_map = {
        'list': JourneyListSerializer,
        'create': JourneyCreateSerializer,
        'update': JourneyUpdateSerializer,
        'partial_update': JourneyUpdateSerializer,
        'retrieve': JourneyDetailSerializer,
    }
    def get_serializer_class(self):
        return self.serializer_map.get(
            self.action, 
            self.serializer_map.get("default")) 
    
