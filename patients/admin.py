from django.contrib import admin

# Register your models here.
from .models import Patient,Appointment

admin.site.register(Patient)
admin.site.register(Appointment)