from django.test import TestCase
from django.urls import reverse

class CapteurUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_capteur_update_page(self):
        response = self.client.get(reverse('capteur_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'capteur/capteur_update.html')