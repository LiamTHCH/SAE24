from django.test import TestCase
from django.urls import reverse

class DataCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_data_create_page(self):
        response = self.client.get(reverse('data_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data/data_create.html')