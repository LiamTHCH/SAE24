from django.test import TestCase
from django.urls import reverse

class DataDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_data_delete_page(self):
        response = self.client.get(reverse('data_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data/data_delete.html')