from rest_framework import serializers

from my_awesome_project.core.models import Journey


class JourneyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = (
            "id",
            "name",
        )
