from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
import json

class TestSetUp(APITestCase):

    def setUp(self):
        user = User(
            email='testing_login@mail.com',
            name='testing_login'
        )
        user.set_password('admin123')
        user.save()

    def test_create_user(self):
        
        client = APIClient()
        response = client.post(
                '/users/create/', {
                'email': 'testing@mail.com',
                'password': 'developer',
                'name': 'jose'
                
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {'name': 'jose',"email":"testing@mail.com"})
    
    def test_login_user(self):

        client = APIClient()
        response = client.post(
                '/users/login/', {
                'email': 'testing_login@mail.com',
                'password': 'admin123',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        result = json.loads(response.content)
        self.assertIn('token', result)