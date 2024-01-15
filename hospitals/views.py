from django.shortcuts import render
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from hospitals.models import Hospital,Department
from hospitals.serializers import HospitalSerializer
from django.http import JsonResponse

from rest_framework import status
# Create your views here.

def GetDoctorsByHospitalAndDepartmentView(request,*args,**kwargs):
    hospital_id = request.GET.get('hospital_id')
    department_id = request.GET.get('department_id')
    if hospital_id and department_id:
        try:
            specific_hospital = Hospital.objects.get(id=hospital_id)
            docs = Doctor.objects.filter(hospitals=specific_hospital,department_id=department_id)
            serialzer = DoctorSerializer(docs,many=True)
            #print(doc)
            #return JsonResponse({'doctors': [{'id': d.id, 'name': d.name} for d in docs]})
            return JsonResponse(serialzer.data,status=200,safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse({'error': 'Doctors not found for the specified hospital and department'}, status=404)
    else:
        return JsonResponse({'error': 'Hospital ID or department not provided'}, status=400)
    
def GetHospitalsByDepartmentView(request,*args,**kwargs):
    department_id = request.GET.get('department_id')
    if department_id:
        try:
            specific_department = Department.objects.get(id=department_id)
            hospitalsByDepartment = Hospital.objects.filter(departments=specific_department)
            serialzer = HospitalSerializer(hospitalsByDepartment,many=True)
            print(serialzer.data)
            return JsonResponse(serialzer.data,status=200,safe=False)
            #return JsonResponse({'hospitals': [{'id': d.id, 'name': d.name} for d in hospitalsByDepartment]})
        except Doctor.DoesNotExist:
            return JsonResponse({'error': 'Doctors not found for the specified hospital and department'}, status=404)
    else:
        return JsonResponse({'error': 'Hospital ID or department not provided'}, status=400)