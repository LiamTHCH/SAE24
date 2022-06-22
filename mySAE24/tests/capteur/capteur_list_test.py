from django.test import TestCase
from django.urls import reverse

class CapteurListTestCase(TestCase):
    def setUp(self):
        pass

    def test_capteur_list_page(self):
        response = self.client.get(reverse('capteur_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'capteur/capteur_list.html')