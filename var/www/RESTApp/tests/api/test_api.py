import requests
import unittest
from . import FlaskAppInstance
BASE = "http://127.0.0.1:5000/"



class FlaskTestCase(unittest.TestCase):


    def setUp(self):
        # creates a test client
        self.app = FlaskAppInstance.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def get_helloworld_test(self):
        #esponse = requests.get(BASE + "helloworld")
        response = self.app.get('/helloworld')
        print(response.json())
        self.assertEqual(response.status_code,200)

if __name__ == "__main__":
    unittest.main()