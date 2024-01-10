# Generated by Django 5.0.1 on 2024-01-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_remove_doctor_hospital_doctor_hospital'),
        ('hospitals', '0004_rename_dname_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.ManyToManyField(db_column='hospital_id', to='hospitals.hospital'),
        ),
    ]
