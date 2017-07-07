# Test Suite
import unittest
from reel import app
from reel.views import signup_welcome


class SignupPageTestClass(unittest.TestCase):

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
    
    def test_signup_status_code(self):
        result = self.app.get('/signup')
         
        self.assertEqual(result.status_code, 200)
        
    def test_signup_welcome_return(self):
        
        self.assertTrue(signup_welcome() == "Welcome to the signup page!")


if __name__ == '__main__':
    unittest.main()
