# Generated by Django 5.0.1 on 2024-01-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_rename_pname_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dateofbirth',
            field=models.DateField(auto_now=True),
        ),
    ]
