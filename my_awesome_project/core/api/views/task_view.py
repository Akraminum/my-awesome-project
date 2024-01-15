from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from my_awesome_project.core.models import Task

from ..serializers.task.list import TaskListSerializer


@extend_schema(tags=['4-Task'])
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
