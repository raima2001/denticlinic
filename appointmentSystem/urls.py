from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('login', views.userlogin, name='login'),
    path('logout', views.logoutuser, name="logout"),
    path('home', views.home, name='home'),
    path('add-doctor', views.add_doctor, name='addDoctor'),
    path('doctor-list', views.list_doctor, name='listDoctor'),
    path('doctor/view/<int:id>', views.view_doctor, name='viewDoctor'),

    path('add-doctor/save', views.save_doctor, name='saveDoctor'),
    path('add-doctor/delete', views.delete_doctor, name='deleteDoctor'),
    path('add-doctor/edit', views.edit_doctor, name='editDoctor'),
    path('timeframe/add', views.add_timeframe, name='addTimeframe'),
    path('timeframe/delete', views.delete_timeframe, name='deleteTimeframe'),

    path('appointment/make', views.makeappointment, name='appointmentMake'),
    path('appointment/view/<int:docid>', views.view_appointments, name='appointmentView'),
    path('appointment/delete', views.delete_appointments, name='appointmentDelete'),
]
