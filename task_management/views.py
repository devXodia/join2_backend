from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

