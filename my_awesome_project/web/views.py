from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect


from my_awesome_project.core.api.views.Journey_view import JourneyViewSet as APIViewSet


class JourneyViewSet(View):
    def get(self, request, *args, **kwargs):
        
        data = {
            "page": "Journey",
            "result": APIViewSet.as_view({'get': 'list'})(request, *args, **kwargs).data,
        }

        return render(request, 'index.html', data)

    def post(self, request, *args, **kwargs):
        return APIViewSet.as_view({'post': 'create'})(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return APIViewSet.as_view({'put': 'update'})(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return APIViewSet.as_view({'delete': 'destroy'})(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return APIViewSet.as_view({'patch': 'partial_update'})(request, *args, **kwargs)
    
    def options(self, request, *args, **kwargs):
        return APIViewSet.as_view({'options': 'retrieve'})(request, *args, **kwargs)
    
    def head(self, request, *args, **kwargs):
        return APIViewSet.as_view({'head': 'retrieve'})(request, *args, **kwargs)
    
    def trace(self, request, *args, **kwargs):
        return APIViewSet.as_view({'trace': 'retrieve'})(request, *args, **kwargs)
    
    def connect(self, request, *args, **kwargs):
        return APIViewSet.as_view({'connect': 'retrieve'})(request, *args, **kwargs)
    
    # /moke/foo
    def moke(self, request, *args, **kwargs):
        return APIViewSet.as_view({'moke': 'retrieve'})(request, *args, **kwargs)
