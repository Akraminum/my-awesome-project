from rest_framework import serializers

from my_awesome_project.core.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "target",
            "name",
        ]
