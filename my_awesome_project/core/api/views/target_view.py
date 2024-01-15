from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from my_awesome_project.core.models import Target

from ..serializers.targets.list import TargetListSerializer


@extend_schema(tags=["3-Target"])
class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetListSerializer
