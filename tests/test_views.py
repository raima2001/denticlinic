from django.test import TestCase, Client
from django.urls import reverse, resolve
from appointmentSystem.views import *
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.doctor = Doctor.objects.create(docname='Test Doc', degree='temp degree')
        self.doctor2 = Doctor.objects.create(docname='Test Doc 3 ', degree='temp degree 3')
        self.tframe = TimeFrame.objects.create(docid=self.doctor, weekday='Tue', starttime='14:00', endtime='16:00')
        self.tframe2 = TimeFrame.objects.create(docid=self.doctor, weekday='Wed', starttime='14:00', endtime='16:00')
        self.appointment = Appointment.objects.create(tframe=self.tframe, pname='Test Patient', pmobile='017000000')
        self.user = User.objects.create(username="testuser")
        self.appointment_url = reverse('appointment')
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.view_doctor_url = reverse('viewDoctor', args=[self.doctor.docid])
        self.list_doctor_url = reverse('listDoctor')
        self.add_doctor_url = reverse('addDoctor')
        self.edit_doctor_url = reverse('editDoctor')
        self.save_doctor_url = reverse('saveDoctor')
        self.delete_doctor_url = reverse('deleteDoctor')
        self.add_timeframe_url = reverse('addTimeframe')
        self.makeappointment_url = reverse('appointmentMake')
        self.delete_appointments_url = reverse('appointmentDelete')
        self.delete_timeframe_url = reverse('deleteTimeframe')
        self.view_appointments_url = reverse('appointmentView', args=[self.doctor.docid])

    def test_appointment(self):
        response = self.client.get(self.appointment_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment.html')

    def test_login(self):
        response = self.client.post(self.login_url, {'username': 'admin', 'password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_makeappointment(self):
        response = self.client.post(self.makeappointment_url,
                                    data={'tfid': self.tframe.tfid, 'pname': 'ABC', 'pmobile': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.appointment_url)

    def test_home_url(self):
        self.client.force_login(self.user)
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_list_doctor(self):
        self.client.force_login(self.user)
        response = self.client.get(self.list_doctor_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor_list.html')

    def test_add_doctor(self):
        self.client.force_login(self.user)
        response = self.client.get(self.add_doctor_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_doctor.html')

    def test_view_doctor(self):
        self.client.force_login(self.user)
        response = self.client.get(self.view_doctor_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_doctor.html')

    def test_edit_doctor(self):
        self.client.force_login(self.user)
        response = self.client.post(self.edit_doctor_url,
                                    data={'docid': self.doctor.docid, 'docname': 'Test Doctor',
                                          'degree': 'Temp Degree'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.view_doctor_url)

    def test_save_doctor(self):
        self.client.force_login(self.user)
        response = self.client.post(self.save_doctor_url,
                                    data={'docname': 'Test Doctor 2', 'degree': 'Temp Degree 2', 'sat_start': '15:00',
                                          'sat_end': '17:00'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.add_doctor_url)

    def test_delete_doctor(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_doctor_url, data={'docid': self.doctor2.docid})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_doctor_url)

    def test_add_timeframe(self):
        self.client.force_login(self.user)
        response = self.client.post(self.add_timeframe_url,
                                    data={'docid': self.doctor.docid, 'weekday': 'Sun', 'starttime': '16:00',
                                          'endtime': '18:00'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.view_doctor_url)

    def test_view_appointments(self):
        self.client.force_login(self.user)
        response = self.client.get(self.view_appointments_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_appointments.html')

    def test_delete_appointments(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_appointments_url,
                                    data={'appid': self.appointment.apid, 'docid': self.doctor.docid})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.view_appointments_url)

    def test_delete_timeframe(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_timeframe_url,
                                    data={'tfid': self.tframe2.tfid, 'docid': self.doctor.docid})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.view_doctor_url)
