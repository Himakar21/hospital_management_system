from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def get_department_id(self):
        return self.id
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department)

    def get_hospital_id(self):
        return self.id
    def __str__(self):
        return self.name