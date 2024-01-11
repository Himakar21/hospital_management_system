from django.db import models
from django.core.validators import RegexValidator
from doctors.models import Doctor
from hospitals.models import Hospital,Department

class Patient(models.Model):

    id = models.AutoField(auto_created=True,primary_key = True)
    name = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    mobilenumber = models.DecimalField(max_digits=10,decimal_places=0)
    def __str__(self):
        return self.name

class Appointment(models.Model):

    status_enum = [('primary check','primary check'),('consultation','consultation'),('admitted','admitted'),('discharged','discharged')]

    id = models.AutoField(auto_created=True,primary_key = True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    symptoms = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,db_column="doctor_id")
    visit_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=status_enum , default="consultation")

    class Meta:
        ordering = ["-visit_date"]