from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Patient,Appointment
from .forms import UpdateAppointmentStatusForm,AddPatientForm,AddAppointmentForm

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer,AppointmentSerializer,UpdateAppointmentStatusSerializer

@login_required(login_url='/')
def HomeView(request,*args,**kwargs):
    return render(request,"home.html",{})

class LoginView(APIView):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html",{"error":"Enter valid credentials"})
    def post(self,request,*args,**kwaargs):
        #print(request.data)#<QUeryDict format>
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        #print(upass,uname)
        user = authenticate(username=uname,password=upass)
        if user:
            login(request,user)
            if user.is_staff:
                return redirect("admin/")
            else:
                return redirect("home/")
        else:
            return render(request,"login.html",{"error":"Incorrect credentials.Please enter valid credentials."})

class SpecificPatientView(APIView):
    def get(self, request,mobile_number, *args, **kwargs):
        try:
            patient = Patient.objects.filter(mobilenumber=mobile_number)
        except Patient.DoesNotExist:
            raise Http404
        serializer = PatientSerializer(patient,many=True)
        #print(serializer.data)
        return render(request,"display_all_patients.html",{"all_patients":serializer.data})

class AllPatientsView(APIView):
    def get(self,request,*args,**kwargs):
        all_patients = Patient.objects.all()
        serializer = PatientSerializer(all_patients,many=True)
        return render(request,"display_all_patients.html",{"all_patients":serializer.data})
    
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

class SpecificAppointmentView(APIView):
    def get(self,request,mobile_number,**kwargs):
        appointments = Appointment.objects.none()
        try:
            # patient_instance=Patient.objects.get(id=id)
            # appointments = Appointment.objects.filter(patient= patient_instance)
            # patients = Patient.objects.filter(mobilenumber=mobile_number)
            # for p in patients:
            #     q = Appointment.objects.filter(patient=p)
            #     appointments = appointments.union(q)
            appointments = Appointment.objects.select_related("patient").filter(patient__mobilenumber=mobile_number)
        except Patient.DoesNotExist:
            raise Http404
        if appointments:
            serializer = AppointmentSerializer(appointments,many=True)
            return render(request,"display_all_appointments.html",{"all_appointments":serializer.data})
        else:
            raise Http404

class AllAppointmentsView(APIView):
    def get(self,request,*args,**kwargs):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments,many=True)
        return render(request,"display_all_appointments.html",{"all_appointments":serializer.data})


class AddSpecificPatientAppointmentView(APIView):
    def get(self,request,id,*args,**kwargs):
        patient = Patient.objects.get(id=id)
        init_patient = {"patient":patient}
        form = AddAppointmentForm(initial=init_patient)
        my_context = {"form":form}
        #print(form.cleaned_data)
        return render(request,"add_appointment.html",my_context)
    def post(self,request,*args,**kwargs):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():#serializer.validated_data attribute contains the cleaned and validated data.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AddAppointmentView(APIView):
    def get(self,request,*args,**kwargs):
        form = AddAppointmentForm()
        my_context = {"form":form}
        #print(form)
        return render(request,"add_appointment.html",my_context)
    def post(self,request,*args,**kwargs):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():#serializer.validated_data attribute contains the cleaned and validated data.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #serializer.errors attribute contains a dictionary where keys are field names, and values are lists of error messages
        

class UpdateStatusView(RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = UpdateAppointmentStatusSerializer
# class UpdateStatusView(APIView):
#     def get(self,request,id):
#         try:
#             instance = Appointment.objects.get(id=id)
#             form = UpdateAppointmentStatusForm(instance=instance)
#             my_context = {"form":form}
#             return render(request,"update_status.html",my_context)
#         except:
#             raise Http404
#     def post(self,request,id):
#         try:
#             instance = Appointment.objects.get(id=id)
#             serializer = AppointmentSerializer(instance=instance,data=request.POST)
#             if serializer.is_valid():
#                 serializer.save()  
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             raise Http404