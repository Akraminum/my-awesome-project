from rest_framework import serializers

from my_awesome_project.core.models import Journey


class JourneyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = (
            "id",
            "name",
        )
