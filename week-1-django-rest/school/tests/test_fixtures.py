from django.test import TestCase
from school.models import Student, Course

class FixturesTestCase(TestCase):
    fixtures = ['prototype_data_base.json']
    
    def test_load_fixtures(self):
        """
        Test if the fixtures are loading correctly.
        """
        student = Student.objects.get(cpf='51684189373')
        course = Course.objects.get(pk=1)
        self.assertEqual(student.cell_phone_number, '59 96638-9981')
        self.assertEqual(course.course_id, 'POO')