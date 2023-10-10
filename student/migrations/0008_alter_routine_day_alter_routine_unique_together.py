# Generated by Django 4.2.5 on 2023-09-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_subject_subject_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='routine',
            unique_together={('which_class', 'day')},
        ),
    ]
