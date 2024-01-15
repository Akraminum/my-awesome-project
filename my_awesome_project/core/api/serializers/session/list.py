from rest_framework import serializers

from my_awesome_project.core.models import Session


class SessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
