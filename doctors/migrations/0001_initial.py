# Generated by Django 5.0.1 on 2024-01-16 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(db_column='department_id', on_delete=django.db.models.deletion.CASCADE, to='hospitals.department')),
                ('hospitals', models.ManyToManyField(db_column='hospital_id', db_table='doctors_doctor_hospital', to='hospitals.hospital')),
            ],
        ),
    ]
