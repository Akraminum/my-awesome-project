from rest_framework import viewsets

from django.contrib.auth.models import User

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
