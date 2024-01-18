"""
URL configuration for hms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from patients.views import SpecificPatientView,AllPatientsView,UpdateStatusView,AddPatientView,HomeView,LoginView,AddAppointmentView,AllAppointmentsView,SpecificAppointmentView,AddSpecificPatientAppointmentView
from hospitals.views import GetDoctorsByHospitalAndDepartmentView,GetHospitalsByDepartmentView

urlpatterns = [
    path('',LoginView.as_view()),
    path('home/',HomeView),
    path('admin/', admin.site.urls),
    path('show_patients/<str:mobile_number>/',SpecificPatientView.as_view()),
    path('show_patients/',AllPatientsView.as_view()),
    path('add_patient/',AddPatientView.as_view()),
    path('show_appointments/<str:mobile_number>/',SpecificAppointmentView.as_view()),
    path('show_appointments/',AllAppointmentsView.as_view()),
    path('add_appointment/',AddAppointmentView.as_view()),
    path('add_appointment/<int:id>',AddSpecificPatientAppointmentView.as_view()),
    path('update_status/<int:id>',UpdateStatusView.as_view()),
    path('get_doctors_by_hospital_and_department/',GetDoctorsByHospitalAndDepartmentView,name='get_hospital_doctors'),
    path('get_hospitals_by_department/',GetHospitalsByDepartmentView,name='get_department_hospitals')
]
