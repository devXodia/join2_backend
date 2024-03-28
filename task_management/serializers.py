from rest_framework import serializers
from .models import Task, Contact
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ContactDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'phone', 'email', 'acronym']


class TaskSerializer(serializers.ModelSerializer):
    assigned_contacts = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'assigned_contacts', 'subtasks', 'category']
