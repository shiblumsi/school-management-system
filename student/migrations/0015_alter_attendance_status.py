# Generated by Django 4.2.5 on 2023-10-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_alter_attendance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], max_length=255),
        ),
    ]
