from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Enrollment, Student, Course
from school.serializers import EnrollmentSerializer

class EnrollmentsTestCase(APITestCase):
    fixtures = ['prototype_data_base.json']
    def setUp(self):
        #self.user = User.objects.create_superuser(username='admin', password='admin')
        self.user = User.objects.get(username='fer')
        self.url = reverse('Enrollments-list')
        self.client.force_authenticate(user=self.user)
        self.student = Student.objects.get(pk=1)
        self.course = Course.objects.get(pk=1)
        self.enrollment = Enrollment.objects.get(pk=1)

    def test_get_request_enrollments(self):
        """
        Test GET request to list enrollments.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_a_enrollment(self):
        """
        Test GET request to an specific enrollment.
        """
        response = self.client.get(self.url+'1/')#/enrollments/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        enrollment_data = Enrollment.objects.get(pk=1)
        enrollment_data_serialized = EnrollmentSerializer(instance=enrollment_data).data
        self.assertEqual(response.data, enrollment_data_serialized)

    def test_post_request_enrollment_create(self):
        """
        Test POST request to create an enrollment.
        """
        data = {
            'student': self.student.pk,
            'course': self.course.pk,
            'shift': 'M'
        }
        response = self.client.post(self.url, data=data)#/enrollments/
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_request_enrollment(self):
        """
        Test DELETE request enrollment.
        """
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_request_enrollment_update(self):
        """
        Test PUT request to update an enrollment.
        """
        data = {
            'student': self.student.pk,
            'course': self.course.pk,
            'shift': 'E'
        }
        response = self.client.put(f'{self.url}1/', data=data)#/enrollments/1/
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)