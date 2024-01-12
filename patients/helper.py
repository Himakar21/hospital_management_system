from patients.models import Patient

def get_patient_by_id(id):
    patient = Patient.objects.get(id=id)
    return patient