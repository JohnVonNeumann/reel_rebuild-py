# Test Suite
import unittest
from reel import app


class GuidePageTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_become_a_guide_status_code(self):
        response = self.app.get('/become_a_guide')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the guide page!", response.data)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
