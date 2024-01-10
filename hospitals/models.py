from django.db import models

# Create your models here.


class Department(models.Model):
    id = models.AutoField(auto_created=True,primary_key = True)
    name = models.CharField(max_length=50)

    def get_department_id(self):
        return self.id
    def __str__(self):
        return self.name

class Hospital(models.Model):
    id = models.AutoField(auto_created=True,primary_key = True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department)

    def get_hospital_id(self):
        return self.id
    def __str__(self):
        return self.name