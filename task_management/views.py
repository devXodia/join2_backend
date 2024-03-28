from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .models import Task, Contact
from .serializers import TaskSerializer, UserSerializer, UserDetailSerializer, ContactDetailsSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer    


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailsSerializer