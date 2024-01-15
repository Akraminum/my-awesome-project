from django.db.models import Q
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from my_awesome_project.core.models import Session

from ..serializers.session.list import SessionListSerializer


@extend_schema(tags=["5-session"])
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionListSerializer

    def get_queryset(self):
        task_id = self.kwargs.get("task_id")
        if task_id:
            return Session.objects.filter(task=Q(id=task_id))
        return Session.objects.all()
