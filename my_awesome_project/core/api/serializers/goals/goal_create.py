from rest_framework import serializers

from my_awesome_project.core.models import Goal

from .goal_details import GoalDetailSerializer


class GoalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ("id", "name", "journey")

    def to_representation(self, instance):
        return GoalDetailSerializer(instance).data
