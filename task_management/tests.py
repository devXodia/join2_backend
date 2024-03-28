from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Task, Subtask
from .serializers import TaskSerializer

class TaskSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            due_date='2022-01-01',
            priority='High'
        )
        self.task.assigned_contacts.add(self.user)
        self.subtask = Subtask.objects.create(task=self.task, title='Test Subtask')

    def test_task_serializer(self):
        serializer = TaskSerializer(instance=self.task)
        self.assertEqual(serializer.data['id'], self.task.id)
        self.assertEqual(serializer.data['title'], 'Test Task')
        self.assertEqual(serializer.data['description'], 'Test description')
        self.assertEqual(serializer.data['due_date'], '2022-01-01')
        self.assertEqual(serializer.data['priority'], 'High')
        self.assertEqual(serializer.data['assigned_contacts'][0]['id'], self.user.id)


