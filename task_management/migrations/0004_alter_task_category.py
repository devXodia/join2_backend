# Generated by Django 4.2.7 on 2024-03-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0003_remove_subtask_task_task_subtasks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Sales', 'Sales'), ('Media', 'Media'), ('Marketing', 'Marketing'), ('Backoffice', 'Backoffice'), ('Design', 'Design'), ('Customer Service', 'Customer Service')], max_length=25),
        ),
    ]
