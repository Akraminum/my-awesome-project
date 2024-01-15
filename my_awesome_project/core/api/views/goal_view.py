from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from my_awesome_project.core.api.serializers.goals.goal_create import GoalCreateSerializer
from my_awesome_project.core.api.serializers.goals.goal_details import GoalDetailSerializer
from my_awesome_project.core.api.serializers.goals.goal_list import GoalListSerializer
from my_awesome_project.core.api.serializers.goals.goal_update import GoalUpdateSerializer
from my_awesome_project.core.models import Goal


@extend_schema(tags=["2-Goals"])
class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalListSerializer

    # filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    # ordering = ['name']

    # serializer_map = {
    #     'list': GoalListSerializer,
    #     'create': GoalCreateSerializer,
    #     'update': GoalUpdateSerializer,
    #     'partial_update': GoalUpdateSerializer,
    #     'retrieve': GoalDetailSerializer,
    # }
    # def get_serializer_class(self, action=None):
    #     if not action:
    #         action = self.action
    #     return self.serializer_map.get(action, self.serializer_map.get("default"))

    # def perform_create(self, serializer):
    #     serializer.save()
    #     serializer = self.get_serializer_class("retrieve")(instance=serializer.instance)
