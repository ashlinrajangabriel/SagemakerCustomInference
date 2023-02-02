####CICD Tests 




import unittest

import requests



class TestEndpoint(unittest.TestCase):



    def setUp(self):

        self.endpoint_url = '<YOUR ENDPOINT URL>'

        self.data = {'input': [1, 2, 3, 4]}



    def test_endpoint_response(self):

        response = requests.post(self.endpoint_url, json=self.data)

        self.assertEqual(response.status_code, 200)



    def test_endpoint_prediction(self):

        response = requests.post(self.endpoint_url, json=self.data)

        prediction = response.json()['prediction']

        self.assertIsInstance(prediction, list)



if __name__ == '__main__':

    unittest.main()

