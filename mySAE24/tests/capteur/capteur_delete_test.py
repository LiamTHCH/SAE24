from django.test import TestCase
from django.urls import reverse

class CapteurDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_capteur_delete_page(self):
        response = self.client.get(reverse('capteur_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'capteur/capteur_delete.html')