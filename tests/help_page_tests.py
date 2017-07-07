# Test Suite
import unittest
from reel import app
from reel.views import help_welcome


class HelpPageTestClass(unittest.TestCase):

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
    
    def test_help_status_code(self):
        result = self.app.get('/help')
         
        self.assertEqual(result.status_code, 200)
        
    def test_help_welcome_return(self):
        
        self.assertTrue(help_welcome() == "Welcome to the help page!")


if __name__ == '__main__':
    unittest.main()
