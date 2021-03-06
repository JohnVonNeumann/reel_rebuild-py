# Test Suite
import unittest
from reel import app


class HomePageTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_response(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Home - Reel", response.data)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
