from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response


from my_awesome_project.core.api.serializers.journey.list import JourneyListSerializer
from my_awesome_project.core.models import Journey


@extend_schema(tags=["1-Journeys"])
class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneyListSerializer

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
    
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = JourneyListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = JourneyListSerializer(queryset, many=True)
        return Response(serializer.data)

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
