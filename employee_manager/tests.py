from rest_framework.test import APITestCase
from .models import Employee
from rest_framework import status


# These tests works without authentication and permissions
class EmployeeAPITest(APITestCase):
    def setUp(self):
        pass

    # Testing employee creation.
    def test_create_emplooyee(self):
        employee = {
            'name': 'Paulo Henrique',
            'email': 'pauloo@amdocs.com',
            'department': 'Backend Developer'
        }

        response = self.client.post('/employee/',employee,format='json') 
    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # Testing employee list. 
    def test_retrieve_employee(self):
        response = self.client.get('employee/1')
        body = response
        print(body)