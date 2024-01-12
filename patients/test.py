from django.test import TestCase#,Client
from patients.helper import get_patient_by_id
from patients.models import Patient
import datetime

class TestPatient(TestCase):
    def setUp(self):
        print("\nsetUp Patient Test case")
        self.patient = Patient.objects.create(
            id=1,
            name="P1",
            dateofbirth = datetime.date(1998, 7, 7),
            mobilenumber = 9876543212
        )
        #self.client = Client()
        pass
    def tearDown(self):
        print("\ntearDown Patient Test case")
        pass
    def test_patient_by_id_is_true(self):
        self.assertEqual(self.patient,get_patient_by_id(1))
    def test_patient_by_id_is_false(self):
        self.assertFalse(True)
    def test_url_status_code_200(self):
        response = self.client.get('/show_patients/')  # Replace with your actual URL
        self.assertEqual(response.status_code, 200)