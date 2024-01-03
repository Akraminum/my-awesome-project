from rest_framework import serializers

from my_awesome_project.core.models import Goal


class GoalBriefSerializer(serializers.ModelSerializer):
    total_targets_count = serializers.IntegerField()
    achieved_targets_count = serializers.IntegerField()

    class Meta:
        model = Goal
        fields = ('id', 'name', "total_targets_count", "achieved_targets_count")  
