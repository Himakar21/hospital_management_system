# Generated by Django 5.0.1 on 2024-01-07 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_remove_patient_department_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
    ]
