from django.test import TestCase
from django.urls import reverse

class CapteurDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_capteur_detail_page(self):
        response = self.client.get(reverse('capteur_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'capteur/capteur_detail.html')