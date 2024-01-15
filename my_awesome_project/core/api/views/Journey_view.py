from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from my_awesome_project.core.api.serializers.journey.list import JourneyListSerializer
from my_awesome_project.core.models import Journey


@extend_schema(tags=["1-Journeys"])
class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneyListSerializer

    # queryset_map = {
    #     'list': Journey.objects.list,
    #     'retrieve': Journey.objects.retrieve,
    #     'create': Journey.objects.all,
    #     'update': Journey.objects.all,
    #     'destroy': Journey.objects.all,
    #     'goals': Journey.objects.all,
    # }
    # serializer_map = {
    #     'list': JourneyListSerializer,
    #     'retrieve': JourneyDetailSerializer,
    #     'create': JourneyCreateSerializer,
    #     'update': JourneyUpdateSerializer,
    #     'destroy': JourneyDetailSerializer,
    #     'goals': JourneyDetailSerializer,
    # }
    # filter_backends = (OrderingFilter,)
    # ordering_fields = ('name',)
    # ordering = ('name',)
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'
    # http_method_names = ['get', 'post', 'put', 'delete']
    # permission_classes = []
    # authentication_classes = []

    # def get_queryset(self):
    #     return self.queryset_map.get(self.action, self.queryset_map['list'])()

    # def get_serializer_class(self):
    #     return self.serializer_map.get(self.action, self.serializer_map['list'])

    # def perform_create(self, serializer):
    #     serializer.save()
    #     serializer = self.get_serializer_class("retrieve")(instance=serializer.instance)
    #     return serializer

    # def perform_update(self, serializer):
    #     serializer.save()
    #     serializer = self.get_serializer_class("retrieve")(instance=serializer.instance)
    #     return serializer

    # @action(detail=True, methods=['get'])
    # def goals(self, request, slug=None):
    #     journey = self.get_object()
    #     goals = journey.goals.all()
    #     serializer = self.get_serializer(goals, many=True)
    #     return Response(serializer.data)
