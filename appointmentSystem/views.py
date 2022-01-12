from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as message_constants
from .models import TimeFrame, Doctor, Appointment
import datetime as dt

MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger', }


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In !!!")
                return redirect('login')
            else:
                messages.warning(request, "Username or Password Incorrect")
                return redirect('login')
    return render(request, 'login.html', {'title': 'Login'})


def logoutuser(request):
    logout(request)
    return redirect('login')


def appointment(request):
    if request.user.is_authenticated:
        return redirect('home')
    data = Doctor.objects.all()
    tframe = TimeFrame.objects.all()
    return render(request, 'appointment.html', {'title': 'Appointment', 'data': data, 'tframe': tframe})


def makeappointment(request):
    if request.method == 'POST':
        tfid = request.POST.get('tfid')
        pname = request.POST.get('pname')
        pmobile = request.POST.get('pmobile')

        tf = TimeFrame.objects.get(tfid=tfid)
        app = Appointment()
        app.tframe = tf
        app.pname = pname
        app.pmobile = pmobile
        app.save()

        messages.success(request, "Appointment Booked Successfully")
        return redirect('appointment')
    else:
        messages.warning(request, "Operation Error !!!")
        redirect('appointment')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'title': 'Home'})


@login_required(login_url='login')
def list_doctor(request):
    data = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'title': 'Doctor List', 'data': data})


@login_required(login_url='login')
def add_doctor(request):
    return render(request, 'add_doctor.html', {'title': 'Add Doctor'})


@login_required(login_url='login')
def view_doctor(request, id):
    data = Doctor.objects.get(docid=id)
    tframe = TimeFrame.objects.filter(docid=data.docid)
    context = {'title': 'View Doctor', 'data': data, 'tframe': tframe}
    return render(request, 'view_doctor.html', context)


@login_required(login_url='login')
def edit_doctor(request):
    if request.method == 'POST':
        docid = request.POST.get('docid')
        docname = request.POST.get('docname')
        degree = request.POST.get('degree')
        doctor = Doctor.objects.get(docid=docid)
        doctor.docname = docname
        doctor.degree = degree
        doctor.save()
        messages.success(request, 'Info Edited Successfully')
        return redirect('viewDoctor', id=request.POST.get('docid'))
    else:
        messages.warning(request, 'Operation Error !!!')
        return redirect('viewDoctor', id=request.POST.get('docid'))


@login_required(login_url='login')
def save_doctor(request):
    if request.method == 'POST':
        docname = request.POST.get('docname')
        degree = request.POST.get('degree')
        sat_start = request.POST.get('sat_start')
        sat_end = request.POST.get('sat_end')
        sun_start = request.POST.get('sun_start')
        sun_end = request.POST.get('sun_end')
        mon_start = request.POST.get('mon_start')
        mon_end = request.POST.get('mon_end')
        tue_start = request.POST.get('tue_start')
        tue_end = request.POST.get('tue_end')
        wed_start = request.POST.get('wed_start')
        wed_end = request.POST.get('wed_end')
        thu_start = request.POST.get('thu_start')
        thu_end = request.POST.get('thu_end')
        fri_start = request.POST.get('fri_start')
        fri_end = request.POST.get('fri_end')

        doctor = Doctor()
        doctor.docname = docname
        doctor.degree = degree
        doctor.save()
        docid = doctor.docid

        if sat_start and sat_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Sat'
            time.starttime = sat_start
            time.endtime = sat_end
            time.save()

        if sun_start and sun_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Sun'
            time.starttime = sun_start
            time.endtime = sun_end
            time.save()

        if mon_start and mon_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Mon'
            time.starttime = mon_start
            time.endtime = mon_end
            time.save()

        if tue_start and tue_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Tue'
            time.starttime = tue_start
            time.endtime = tue_end
            time.save()

        if wed_start and wed_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Wed'
            time.starttime = wed_start
            time.endtime = wed_end
            time.save()

        if thu_start and thu_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Thu'
            time.starttime = thu_start
            time.endtime = thu_end
            time.save()

        if fri_start and fri_end:
            time = TimeFrame()
            time.docid = doctor
            time.weekday = 'Fri'
            time.starttime = fri_start
            time.endtime = fri_end
            time.save()

        messages.warning(request, "Doctor Added Successfully")
        return redirect('addDoctor')
    else:
        messages.warning(request, "Operation Error !!!")
        return redirect('addDoctor')


@login_required(login_url='login')
def delete_doctor(request):
    if request.method == 'POST':
        docid = request.POST.get('docid')
        doctor = Doctor.objects.get(docid=docid)
        doctor.delete()
        messages.success(request, 'Doctor Deleted Successfully')
        return redirect('listDoctor')
    else:
        messages.warning(request, 'Operation Error !!!')
        return redirect('listDoctor')


@login_required(login_url='login')
def add_timeframe(request):
    if request.method == 'POST':
        flag = 0
        docid = request.POST.get('docid')
        weekday = request.POST.get('weekday')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        timeframes = TimeFrame.objects.filter(docid=docid)
        doctor = Doctor.objects.get(docid=docid)

        for item in timeframes:
            if weekday == item.weekday:
                flag = flag + 1

        if flag == 0:
            tf = TimeFrame()
            tf.weekday = weekday
            tf.docid = doctor
            tf.starttime = starttime
            tf.endtime = endtime
            tf.save()
        else:
            messages.warning(request, 'Weekday Already Exists')
            return redirect('viewDoctor', request.POST.get('docid'))

        messages.success(request, 'New Timeframe Added')
        return redirect('viewDoctor', request.POST.get('docid'))
    else:
        messages.warning(request, 'Operation Error !!!')
        return redirect('viewDoctor', request.POST.get('docid'))


@login_required(login_url='login')
def view_appointments(request, docid):
    doctor = Doctor.objects.get(docid=docid)
    tframe = TimeFrame.objects.filter(docid=doctor)
    data = Appointment.objects.filter()
    today = dt.datetime.today().strftime('%a')
    context = {'title': 'Todays Appointments', 'data': data, 'tframe': tframe, 'docid': docid, 'doctor': doctor,
               'today': today}
    return render(request, 'view_appointments.html', context)


@login_required(login_url='login')
def delete_appointments(request):
    if request.method == 'POST':
        appid = request.POST.get('appid')
        app = Appointment.objects.get(apid=appid)
        app.delete()
        messages.success(request, 'Appointment Deleted Successfully')
        return redirect('appointmentView', docid=request.POST.get('docid'))
    else:
        messages.warning(request, 'Operation Error !!!')
        return redirect('appointmentView', docid=request.POST.get('docid'))


@login_required(login_url='login')
def delete_timeframe(request):
    if request.method == 'POST':
        tf = TimeFrame.objects.get(tfid=request.POST.get('tfid'))
        tf.delete()
        messages.success(request, 'Timeframe Deleted Successfully')
        return redirect('viewDoctor', id=request.POST.get('docid'))
    else:
        return redirect('logout')
