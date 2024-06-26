# Generated by Django 4.2.7 on 2024-03-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0010_alter_task_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=3)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Customer Service', 'Customer Service'), ('Backoffice', 'Backoffice'), ('Design', 'Design'), ('Sales', 'Sales'), ('Media', 'Media')], max_length=25),
        ),
    ]
