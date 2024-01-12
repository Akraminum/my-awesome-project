from rest_framework import viewsets
from drf_spectacular.utils import extend_schema


from my_awesome_project.core.models import Target

from ..serializers.target.list import TargetListSerializer


@extend_schema(tags=['3-Target'])
class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetListSerializer