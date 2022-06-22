from django.test import TestCase
from django.urls import reverse

class DataListTestCase(TestCase):
    def setUp(self):
        pass

    def test_data_list_page(self):
        response = self.client.get(reverse('data_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data/data_list.html')