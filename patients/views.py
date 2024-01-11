from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from .models import Patient,Appointment
from .forms import UpdateAppointmentStatusForm,AddPatientForm,AddAppointmentForm

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer,AppointmentSerializer

def HomeView(request,*args,**kwargs):
    return render(request,"home.html",{})

def LoginView(request,*args,**kwargs):
    if request.method=="POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        user = authenticate(username=uname,password=upass)
        if user:
            login(request,user)
            return redirect("home/")

    return render(request,"login.html",{})

class SpecificPatientView(RetrieveAPIView):
    def get(self, request, id, *args, **kwargs):
        try:
            patient = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            raise Http404
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

class AllPatientsView(APIView):
    def get(self,request,*args,**kwargs):
        all_patients = Patient.objects.all()
        serializer = PatientSerializer(all_patients,many=True)
        return Response(serializer.data)
    
class AddPatientView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        form = AddPatientForm()
        my_context = {"form": form}
        return render(request, "add_patient.html", my_context)

class SpecificAppointmentView(RetrieveAPIView):
    def get(self,request,id,**kwargs):
        try:
            appointment = Appointment.objects.get(id=id)
        except Patient.DoesNotExist:
            raise Http404
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

class AllAppointmentsView(APIView):
    def get(self,request,*args,**kwargs):
        all_appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(all_appointments,many=True)
        #print(serializer)
        return Response(serializer.data)

class AddAppointmentView(APIView):
    def get(self,request,*args,**kwargs):
        form = AddAppointmentForm()
        my_context = {"form":form}
        #print(form)
        return render(request,"add_appointment.html",my_context)
    def post(self,request,*args,**kwargs):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateStatusView(APIView):
    def get(self,request,id):
        form = UpdateAppointmentStatusForm()
        #print(form.data)
        my_context = {"form":form}
        return render(request,"update_status.html",my_context)
    def post(self,request,id):
        instance = Appointment.objects.get(id=id)
        #print(request.POST)
        form = UpdateAppointmentStatusForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  
            serializer = AppointmentSerializer(instance) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)