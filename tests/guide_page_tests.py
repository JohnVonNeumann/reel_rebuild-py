# Test Suite
import unittest
from reel import app
from reel.views import guide_welcome


class GuidePageTestClass(unittest.TestCase):

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
    
    def test_become_a_guide_status_code(self):
        result = self.app.get('/become_a_guide')
         
        self.assertEqual(result.status_code, 200)
        
    def test_guide_welcome_return(self):
        
        self.assertTrue(guide_welcome() == "Welcome to the guide page!")


if __name__ == '__main__':
    unittest.main()
