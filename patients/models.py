from django.db import models
from doctors.models import Doctor
from hospitals.models import Hospital,Department

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date, timedelta

class Patient(models.Model):
    mobilenumber_validator = RegexValidator(
        regex=r'^[1-9]\d{9}$',
        message="10 digit number",
    )
    def validate_age(value):
        today = date.today()
        age_limit = timedelta(days=365 * 150)  # 150 years
        if (value > today) or ((today - value) > age_limit):
            raise ValidationError('Invalid date of birth.')#excpet raise ValidationError every other ereturn values are true

    name = models.CharField(max_length=50)
    dateofbirth = models.DateField(validators=[validate_age])
    mobilenumber = models.CharField(max_length=10,validators=[mobilenumber_validator])
    def __str__(self):
        return self.name
    def get_age(self):
        return date.today()-self.dateofbirth

class Appointment(models.Model):

    status_enum = [('primary check','primary check'),('consultation','consultation'),('admitted','admitted'),('discharged','discharged')]

    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    symptoms = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,db_column="doctor_id")
    visit_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=status_enum , default="consultation")

    class Meta:
        ordering = ["-visit_date"]