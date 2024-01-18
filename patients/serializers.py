from rest_framework import serializers
from patients.models import Patient,Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
    #to_representation() method is called by DRF just before serializing the data.
    #it gives you an opportunity to modify the data in any way you want.
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['patient'] = instance.patient.__str__()  
        representation['doctor'] = instance.doctor.__str__()
        representation['hospital'] = instance.hospital.__str__()   
        representation['department'] = instance.department.__str__()     
        return representation