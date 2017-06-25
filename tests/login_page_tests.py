# Test Suite
import unittest
from reel.run import app, login_welcome


class LoginPageTestClass(unittest.TestCase):

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
    
    def test_login_status_code(self):
        result = self.app.get('/login')
         
        self.assertEqual(result.status_code, 200)
        
    def test_login_welcome_return(self):
        
        self.assertTrue(login_welcome() == "Welcome to the login page!")


if __name__ == '__main__':
    unittest.main()
