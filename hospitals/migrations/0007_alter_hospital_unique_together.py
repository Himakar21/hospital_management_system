# Generated by Django 5.0.1 on 2024-01-10 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0006_alter_hospital_address'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hospital',
            unique_together=set(),
        ),
    ]
