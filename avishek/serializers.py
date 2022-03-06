from .models import Project, Contact
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContactSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
