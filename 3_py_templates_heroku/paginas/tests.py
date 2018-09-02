from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase


class SimpleTest(SimpleTestCase):
    def test_inicio(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_sobre_mi(self):
        response = self.client.get('/sobremi/')
        self.assertEqual(response.status_code,200)
