from django.shortcuts import render
from doctors.models import Doctor
from hospitals.models import Hospital,Department
from django.http import JsonResponse
# Create your views here.

def GetDoctorsByHospitalAndDepartmentView(request,*args,**kwargs):
    hospital_id = request.GET.get('hospital_id')
    department_id = request.GET.get('department_id')
    if hospital_id and department_id:
        try:
            specific_hospital = Hospital.objects.get(id=hospital_id)
            doc = Doctor.objects.filter(hospitals=specific_hospital,department_id=department_id)
            #print(doc)
            return JsonResponse({'doctors': [{'id': d.id, 'name': d.name} for d in doc]})
        except Doctor.DoesNotExist:
            return JsonResponse({'error': 'Doctors not found for the specified hospital and department'}, status=404)
    else:
        return JsonResponse({'error': 'Hospital ID or department not provided'}, status=400)
    
def GetHospitalsByDepartmentView(request,*args,**kwargs):
    department_id = request.GET.get('department_id')
    if department_id:
        try:
            specific_department = Department.objects.get(id=department_id)
            hospitalByDepartment = Hospital.objects.filter(departments=specific_department)
            return JsonResponse({'hospitals': [{'id': h.id, 'name': h.name} for h in hospitalByDepartment]})
        except Doctor.DoesNotExist:
            return JsonResponse({'error': 'Doctors not found for the specified hospital and department'}, status=404)
    else:
        return JsonResponse({'error': 'Hospital ID or department not provided'}, status=400)