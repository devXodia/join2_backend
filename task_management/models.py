from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    due_date = models.DateField()
    category = models.CharField(max_length=25, choices=[
        ('Media', 'Media'),
        ('Design', 'Design'),
        ('Customer Service', 'Customer Service'),
        ('Backoffice', 'Backoffice'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
    ])
    priority = models.CharField(max_length=20, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])
    assigned_contacts = models.ManyToManyField(User, related_name='assigned_tasks')
    subtasks = models.JSONField(default=None)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    acronym = models.CharField(max_length = 3)
    phone = models.IntegerField()
    email = models.CharField(max_length = 30)


