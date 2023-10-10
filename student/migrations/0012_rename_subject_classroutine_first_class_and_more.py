# Generated by Django 4.2.5 on 2023-09-18 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_classroutine_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroutine',
            old_name='subject',
            new_name='first_class',
        ),
        migrations.RemoveField(
            model_name='classroutine',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='classroutine',
            name='fifth_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_class', to='student.subject'),
        ),
        migrations.AddField(
            model_name='classroutine',
            name='fourth_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_class', to='student.subject'),
        ),
        migrations.AddField(
            model_name='classroutine',
            name='second_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_class', to='student.subject'),
        ),
        migrations.AddField(
            model_name='classroutine',
            name='sixth_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sixth_class', to='student.subject'),
        ),
        migrations.AddField(
            model_name='classroutine',
            name='third_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_class', to='student.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='time_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time_slot', to='student.routinetimeslot'),
        ),
    ]
