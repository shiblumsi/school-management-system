# Generated by Django 4.2.5 on 2023-09-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_routine_day_alter_routine_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutineTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_time', models.CharField(max_length=255)),
            ],
        ),
    ]
