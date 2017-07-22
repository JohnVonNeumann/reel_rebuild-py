# Test Suite
import unittest
from reel import app


class HelpPageTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_help_status_code(self):
        response = self.app.get('/help')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Help - Reel", response.data)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
