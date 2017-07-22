# Test Suite
import unittest
from reel import app


class HomePageTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_response(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Welcome to Reel!", result.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    print(test_homepage_response.result)
