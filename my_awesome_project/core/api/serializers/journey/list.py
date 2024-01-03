from rest_framework import serializers

from my_awesome_project.core.models import Journey


class JourneyListSerializer(serializers.ModelSerializer):
    goals_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Journey
        fields = ("id", "name", "goals_count", "created")
