from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SuccessfulMessageTest(APITestCase):
    def setUp(self):
        self.url = reverse("echo_message")
        self.data = {
            'message': 'Hello World!'
        }
        self.response = self.client.post(self.url, self.data, format='json')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK) 
    
    def test_data_received(self):
        self.assertEqual(self.data, self.response.data)


class FailedMessageTest(APITestCase):
    def setUp(self):
        self.url = reverse("echo_message")
        self.data = {
            'mesage': 'Hello World!'
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.error_message = {
            'message': [
                'This field is required'
            ]
        }

    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST) 
