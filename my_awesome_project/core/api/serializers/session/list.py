from rest_framework import serializers

from my_awesome_project.core.models import Session


class SessionListSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="task.name")
    class Meta:
        model = Session
        fields = [
            "id",
            "task_name",
            "minutes",
            "datetime",
        ]