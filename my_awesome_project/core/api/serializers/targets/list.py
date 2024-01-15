from rest_framework import serializers
from my_awesome_project.core.models import Target

class TargetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"