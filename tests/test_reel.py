# Test Suite
import unittest

class MyTestClass(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_equal_numbers(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
