from rest_framework import serializers

from my_awesome_project.core.models import Session, Task

from ..task.nested import TaskBriefSerializer


class SessionListSerializer(serializers.ModelSerializer):
    # task = TaskBriefSerializer(read_only=True)
    # task_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), write_only=True)
    class Meta:
        model = Session
        fields = [
            "id",
            "task",
            # "task_id",
            "minutes",
            "datetime",
        ]
