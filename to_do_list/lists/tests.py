from django.test import TestCase


class SmokeTest(TestCase):
    def test_math(self):
        self.assertEqual(2, 3)
