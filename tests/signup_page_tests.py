# Test Suite
import unittest
from reel import app


class SignupPageTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_signuppage_response(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the signup page!", response.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
