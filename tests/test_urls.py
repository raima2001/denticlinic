from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appointmentSystem.views import *


class TestUrls(SimpleTestCase):
    def test_appointment(self):
        url = reverse('appointment')
        self.assertEquals(resolve(url).func, appointment)

    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, userlogin)

    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutuser)

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_addoctor(self):
        url = reverse('addDoctor')
        self.assertEquals(resolve(url).func, add_doctor)

    def test_listdoctor(self):
        url = reverse('listDoctor')
        self.assertEquals(resolve(url).func, list_doctor)

    def test_viewdoctor(self):
        url = reverse('viewDoctor', args=[10])
        self.assertEquals(resolve(url).func, view_doctor)

    def test_savedoctor(self):
        url = reverse('saveDoctor')
        self.assertEquals(resolve(url).func, save_doctor)

    def test_deletedoctor(self):
        url = reverse('deleteDoctor')
        self.assertEquals(resolve(url).func, delete_doctor)

    def test_editdoctor(self):
        url = reverse('editDoctor')
        self.assertEquals(resolve(url).func, edit_doctor)

    def test_addtimeframe(self):
        url = reverse('addTimeframe')
        self.assertEquals(resolve(url).func, add_timeframe)

    def test_deletetimeframe(self):
        url = reverse('deleteTimeframe')
        self.assertEquals(resolve(url).func, delete_timeframe)

    def test_makeappointment(self):
        url = reverse('appointmentMake')
        self.assertEquals(resolve(url).func, makeappointment)

    def test_viewappointment(self):
        url = reverse('appointmentView', args=[10])
        self.assertEquals(resolve(url).func, view_appointments)

    def test_deleteappointment(self):
        url = reverse('appointmentDelete')
        self.assertEquals(resolve(url).func, delete_appointments)
