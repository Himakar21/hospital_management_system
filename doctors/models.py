from django.db import models

from hospitals.models import Hospital,Department

class Doctor(models.Model):
    id = models.AutoField(auto_created=True,primary_key = True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,db_column="department_id")
    hospitals = models.ManyToManyField(Hospital,db_column="hospital_id",db_table="doctors_doctor_hospital")

    def __str__(self):
        return self.name
    