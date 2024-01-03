from rest_framework import serializers

from my_awesome_project.core.models import Goal
from my_awesome_project.core.api.serializers.journey.detail import JourneyDetailSerializer



class GoalListSerializer(serializers.ModelSerializer):
    journey = JourneyDetailSerializer()

    class Meta:
        model = Goal
        fields = '__all__'