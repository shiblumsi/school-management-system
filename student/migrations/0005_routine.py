# Generated by Django 4.2.5 on 2023-09-17 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_examtype_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=255)),
                ('which_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classroom')),
            ],
        ),
    ]