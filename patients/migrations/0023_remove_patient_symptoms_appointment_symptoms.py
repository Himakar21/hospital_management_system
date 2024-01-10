# Generated by Django 5.0.1 on 2024-01-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_alter_patient_options_remove_patient_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
        migrations.AddField(
            model_name='appointment',
            name='symptoms',
            field=models.TextField(default='Fever'),
            preserve_default=False,
        ),
    ]
