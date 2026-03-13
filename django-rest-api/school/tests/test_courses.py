from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Course
from school.serializers import CourseSerializer

class CoursesTestCase(APITestCase):
    fixtures = ['prototype_data_base.json']
    def setUp(self):
        #self.user = User.objects.create_superuser(username='admin', password='admin')
        self.user = User.objects.get(username='fer')
        self.url = reverse('Courses-list')
        self.client.force_authenticate(user=self.user)
        self.course_01 = Course.objects.get(pk=1)
        self.course_02 = Course.objects.get(pk=2)

    def test_get_request_courses(self):
        """
        Test GET request to list courses.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_a_course(self):
        """
        Test GET request to an specific course.
        """
        response = self.client.get(self.url+'1/')#/courses/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        course_data = Course.objects.get(pk=1)
        course_data_serialized = CourseSerializer(instance=course_data).data
        self.assertEqual(response.data, course_data_serialized)

    def test_post_request_course_create(self):
        """
        Test POST request to create a course.
        """
        data = {
            'course_id': 'TestCreate',
            'description': 'Description for Test Course Creation',
            'level': 'B'
        }
        response = self.client.post(self.url, data=data)#/courses/
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_request_course(self):
        """
        Test DELETE request course.
        """
        response = self.client.delete(f'{self.url}2/')#/courses/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_request_course_update(self):
        """
        Test PUT request to update a course.
        """
        data = {
            'course_id': 'Test PUT',
            'description': 'Description for Test Course update',
            'level': 'A'
        }
        response = self.client.put(f'{self.url}1/', data=data)#/courses/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)       
    

