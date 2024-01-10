from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from .models import Patient,Appointment
from .forms import UpdateAppointmentStatusForm,AddPatientForm,AddAppointmentForm

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

def SpecificPatientView(request,id,**kwargs):
    try:
        pat = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        raise Http404
    my_context = {"patient":pat}
    return render(request,"display_specific_patient.html",my_context)

def AllPatientsView(request,*args,**kwargs):
    all_patients = Patient.objects.all()
    my_context = {"all_patients":all_patients}
    #print(all_patients)
    return render(request,"display_all_patients.html",my_context)

def AddPatientView(request,*args,**kwargs):
    form = AddPatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddPatientForm()
    else:
        print(form.errors)
    my_context = {"form":form}
    #print(form)
    return render(request,"add_patient.html",my_context)

def SpecificAppointmentView(request,id,**kwargs):
    try:
        appointment = Appointment.objects.get(id=id)
    except Patient.DoesNotExist:
        raise Http404
    my_context = {"appointment":appointment}
    return render(request,"display_specific_appointment.html",my_context)

def AllAppointmentsView(request,*args,**kwargs):
    all_appointments = Appointment.objects.all()
    my_context = {"all_appointments":all_appointments}
    #print(all_patients)
    return render(request,"display_all_appointments.html",my_context)

def AddAppointmentView(request,*args,**kwargs):
    form = AddAppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddAppointmentForm()
    else:
        print(form.errors)
    my_context = {"form":form}
    #print(form)
    return render(request,"add_appointment.html",my_context)

def UpdateStatusView(request,id):
    form = UpdateAppointmentStatusForm(request.POST or None,instance=Appointment.objects.get(id=id))
    if form.is_valid():
        form.save()
        #my_context = {"patient":Patient.objects.get(id=id)}
        return render(request,"display_all_patients.html",my_context)
    else:
        print(form.errors)
        print("error")
    my_context={"form":form}
    return render(request,"update_status.html",my_context)