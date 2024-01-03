from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from my_awesome_project.core.models import Goal

from my_awesome_project.core.api.serializers.goals.goal_list import GoalListSerializer
from my_awesome_project.core.api.serializers.goals.goal_create import GoalCreateSerializer
from my_awesome_project.core.api.serializers.goals.goal_update import GoalUpdateSerializer
from my_awesome_project.core.api.serializers.goals.goal_details import GoalDetailSerializer


class GoalViewSet(viewsets.ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    ordering = ['name']
    
    queryset = Goal.objects.all()
    serializer_map = {
        'list': GoalListSerializer,
        'create': GoalCreateSerializer,
        'update': GoalUpdateSerializer,
        'partial_update': GoalUpdateSerializer,
        'retrieve': GoalDetailSerializer,
    }
    def get_serializer_class(self, action=None):
        if not action:
            action = self.action
        return self.serializer_map.get(action, self.serializer_map.get("default")) 
    
    def perform_create(self, serializer):
        serializer.save()
        serializer = self.get_serializer_class("retrieve")(instance=serializer.instance)
        