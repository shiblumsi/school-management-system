# Generated by Django 4.2.5 on 2023-09-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_examtype_alter_subject_which_class_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='year',
            field=models.IntegerField(),
        ),
    ]