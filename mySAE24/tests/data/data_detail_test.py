from django.test import TestCase
from django.urls import reverse

class DataDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_data_detail_page(self):
        response = self.client.get(reverse('data_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data/data_detail.html')