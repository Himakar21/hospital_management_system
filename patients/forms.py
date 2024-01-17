from django import forms
from patients.models import Patient,Appointment
    

class UpdateAppointmentStatusForm(forms.ModelForm):            
    class Meta():
        model = Appointment
        fields = ['patient', 'symptoms', 'department', 'hospital', 'doctor','status']
        
    
class AddPatientForm(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['name','mobilenumber','dateofbirth']

class AddAppointmentForm(forms.ModelForm):
    class Meta():
        model = Appointment
        fields = ['patient','symptoms','department','hospital','doctor','status']