from unittest import TestCase
from django.test import Client
from eroster.models import Agency

class AgencyTest(TestCase):

    """ Test module for Agency model """

    def setUp(self):
        Agency.objects.create(
            name='UNICEF', country='Madagascar')
        Agency.objects.create(
            name='UNDP', country='Madagascar')

    def test_agency_creation(self):
        self.assertEqual(Agency.objects.count(), 2)

    def test_string_representation(self):
        agency = Agency(name="My Agency name")
        self.assertEqual(str(agency), agency.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Agency._meta.verbose_name_plural), "Agencies")
    
    