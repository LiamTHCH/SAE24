from django.test import TestCase
from django.urls import reverse

class CapteurCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_capteur_create_page(self):
        response = self.client.get(reverse('capteur_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'capteur/capteur_create.html')