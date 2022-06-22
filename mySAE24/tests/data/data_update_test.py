from django.test import TestCase
from django.urls import reverse

class DataUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_data_update_page(self):
        response = self.client.get(reverse('data_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data/data_update.html')