# Test Suite
import unittest
from reel.run import app, hello_world


class MyTestClass(unittest.TestCase):

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
        
    def test_hello_world_return(self):
        
        self.assertTrue(hello_world() == "Hello, World!")


if __name__ == '__main__':
    unittest.main()
