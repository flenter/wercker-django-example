from django.test.client import Client
from django.test import TestCase


class HomeTest(TestCase):
    fixtures = ["cities.json"]

    def test_has_world(self):
        c = Client()

        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "world")

    def test_has_amsterdam(self):
        c = Client()

        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Amsterdam")
