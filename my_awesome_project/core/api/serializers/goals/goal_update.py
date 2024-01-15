from rest_framework import serializers

from my_awesome_project.core.models import Goal


class GoalUpdateSerializer(serializers.ModelSerializer):
    ...

    class Meta:
        model = Goal
        fields = "__all__"
