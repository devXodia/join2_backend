# Generated by Django 4.2.7 on 2024-03-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0004_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Design', 'Design'), ('Backoffice', 'Backoffice'), ('Customer Service', 'Customer Service'), ('Media', 'Media')], max_length=25),
        ),
    ]
