from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student
from school.serializers import StudentSerializer

class StudentsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Students-list')
        self.client.force_authenticate(user=self.user)
        self.student_01 = Student.objects.create(
            first_name='Test Student',
            last_name='One',
            email='test1@example.com',
            cpf='59812748083', date_of_birth='2000-01-01',
            cell_phone_number='86 99999-9999'
        )
        self.student_02 = Student.objects.create(
            first_name='Test Student',
            last_name='Two',
            email='test2@example.com',
            cpf='02139023030', date_of_birth='2000-01-01',
            cell_phone_number='86 99999-9999'
        )
    
    def test_get_request_students(self):
        """
        Test GET request to list students.
        """
        response = self.client.get(self.url)#/students/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_a_student(self):
        """
        Test GET request to an specific student.
        """
        response = self.client.get(self.url+'1/')#/students/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        student_data = Student.objects.get(pk=1)
        student_data_serialized = StudentSerializer(instance=student_data).data
        self.assertEqual(response.data, student_data_serialized)

    def test_post_request_student_criate(self):
        """
        Test POST request to create a student.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'Student',
            'email': 'test3@example.com',
            'cpf': '30544541006',
            'date_of_birth': '2000-01-01',
            'cell_phone_number': '86 99999-9999'
        }
        response = self.client.post(self.url, data=data)#/students/
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_request_studen(self):
        """
        Test DELETE request student.
        """
        response = self.client.delete(f'{self.url}2/')#/students/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_request_student_update(self):
        """
        Test PUT request to update a student.
        """
        data = {
            'first_name': 'TestPut',
            'last_name': 'Student',
            'email': 'testput@example.com',
            'cpf': '05790777058',
            'date_of_birth': '2000-01-01',
            'cell_phone_number': '86 99999-9999'
        }
        response = self.client.put(f'{self.url}1/', data=data)#/students/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
