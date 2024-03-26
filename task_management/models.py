from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])
    assigned_contacts = models.ManyToManyField(User, related_name='assigned_tasks')
    

    def __str__(self):
        return self.title
    

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title