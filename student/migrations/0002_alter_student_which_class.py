# Generated by Django 4.2.5 on 2023-09-16 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='which_class',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='student.classroom'),
        ),
    ]
