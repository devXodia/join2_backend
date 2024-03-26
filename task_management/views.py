from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Task, Subtask
from .serializers import TaskSerializer, UserSerializer, SubtaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer