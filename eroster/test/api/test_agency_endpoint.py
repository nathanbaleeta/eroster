from django.shortcuts import reverse
from rest_framework.test import APITestCase
from eroster.models import Agency

class AgencyEndpointTest(APITestCase):
    def setUp(self):
        # create movie
        self.agency = Agency(name="UNICEF", country='Madagascar')
        self.agency.save()

    def test_agency_creation(self):
        response = self.client.post(reverse('agencies'), {
            'name': 'UNICEF',
            'country': 'Madagascar'
        })

        # assert new agency was added
        self.assertEqual(Agency.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_agencies(self):
        response = self.client.get(reverse('agencies'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_agency(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'name': 'UNDP',
            'country': 'Uganda'
        }, format="json")

        # check info returned has the update
        self.assertEqual('undp', response.data['name'])

    def test_deleting_agency(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)
        
