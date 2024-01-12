from rest_framework import serializers

from my_awesome_project.core.models import Journey
from my_awesome_project.core.api.serializers.goals.brief import GoalBriefSerializer


class JourneyDetailSerializer(serializers.ModelSerializer):
    # goals = GoalBriefSerializer(many=True)

    class Meta:
        model = Journey
        fields = ("id", "name", "goals")