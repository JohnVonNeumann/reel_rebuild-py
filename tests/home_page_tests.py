# Test Suite
import unittest
from reel import app
from reel.views import home_welcome


class HomePageTesttClass(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200)

    def test_home_welcome_return(self):
        response = self.app.get('/')
        self.assertIn(b"Welcome to Reel!", response.data)


if __name__ == '__main__':
    unittest.main()
