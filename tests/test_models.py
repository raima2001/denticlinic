from django.test import TestCase
from appointmentSystem.models import *
from django.contrib.auth.models import User


class TestModels(TestCase):
    def test_create_doctor(self):
        self.doctor = Doctor.objects.create(docname='ABC', degree='Demo Degree')
        self.assertEquals(self.doctor.docname, 'ABC')

    def test_create_timeframe(self):
        self.test_create_doctor()
        self.tframe = TimeFrame.objects.create(docid=self.doctor, weekday='Wed', starttime='16:00', endtime='18:00')
        self.assertEquals(self.tframe.weekday, 'Wed')

    def test_create_appointment(self):
        self.test_create_timeframe()
        self.appointment = Appointment.objects.create(tframe=self.tframe, pname='Test Patient', pmobile='01700000')
        self.assertEquals(self.appointment.pname, 'Test Patient')
