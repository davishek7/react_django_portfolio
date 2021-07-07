from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContactSerailizer(serializers.Serializer):
    name = serializers.CharField()
    subject = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()