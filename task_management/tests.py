from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Task, Contact
from .serializers import TaskSerializer, ContactDetailsSerializer, UserSerializer

class TaskSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            due_date='2022-01-01',
            priority='High',
            subtasks={'subtasks': [{'subtask_name': 'test subtask', 'completed': True}]}
        )
        self.task.assigned_contacts.add(self.user)

    def test_task_serializer(self):
        serializer = TaskSerializer(instance=self.task)
        self.assertEqual(serializer.data['id'], self.task.id)
        self.assertEqual(serializer.data['title'], 'Test Task')
        self.assertEqual(serializer.data['description'], 'Test description')
        self.assertEqual(serializer.data['due_date'], '2022-01-01')
        self.assertEqual(serializer.data['priority'], 'High')
        self.assertEqual(serializer.data['assigned_contacts'][0]['id'], self.user.id)

class CreateUserSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', email='testemail@email.de')
        self.user.set_password('testpassword')

    def test_user_create_serializer(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(serializer.data['username'], 'test_user')
        self.assertEqual(serializer.data['email'], 'testemail@email.de')
        self.assertTrue(self.user.check_password('testpassword'))


class CreateContactTest(APITestCase):
    def setUp(self):
        self.contact = Contact.objects.create(name= "Alen", last_name= "Alduk", email= "test@email.de", acronym= "AA", phone= "017644444444")


    def test_create_contact(self):
        serializer = ContactDetailsSerializer(instance=self.contact)
        self.assertEqual(serializer.data['name'], 'Alen')
        self.assertEqual(serializer.data['last_name'], 'Alduk')
        self.assertEqual(serializer.data['email'], 'test@email.de')
        self.assertEqual(serializer.data['acronym'], 'AA')
        self.assertEqual(serializer.data['phone'], '017644444444')