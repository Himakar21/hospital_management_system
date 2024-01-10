from django import forms
from django.core.validators import RegexValidator
from doctors.models import Doctor
from patients.models import Patient,Appointment
    

class UpdateAppointmentStatusForm(forms.ModelForm):
    class Meta():
        model = Appointment
        fields = ['status']
    
class AddPatientForm(forms.ModelForm):
    mobilenumber_validator = RegexValidator(
        regex=r'^[1-9]\d{9}$',
        message="10 digit number",
    )
    mobilenumber = forms.DecimalField(max_digits=10,decimal_places=0,validators=[mobilenumber_validator])
    class Meta():
        model = Patient
        fields = ['name','mobilenumber','dateofbirth']

class AddAppointmentForm(forms.ModelForm):
    class Meta():
        model = Appointment
        fields = ['patient','symptoms','department','hospital','doctor','status']