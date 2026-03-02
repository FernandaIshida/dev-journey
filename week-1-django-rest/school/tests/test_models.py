from django.test import TestCase
from school.models import Student, Course, Enrollment

class StudentModelTestCase(TestCase):
    #def test_failure(self):
    #    self.fail('Test failed')
    def setUp(self):
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='2000-01-01',
            email='john.doe@example.com',
            cpf='38337731036',
            cell_phone_number='86 99999-9999')
        
    def test_student_creation(self):
        """
        The test verifies attributes of the Student model.
        """
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.last_name, 'Doe')
        self.assertEqual(self.student.date_of_birth, '2000-01-01')
        self.assertEqual(self.student.email, 'john.doe@example.com')
        self.assertEqual(self.student.cpf, '38337731036')
        self.assertEqual(self.student.cell_phone_number, '86 99999-9999')

class CourseModelTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            course_id='ex301',
            description='Example course description',
            level='B')

    def test_course_creation(self):
        """
        The test verifies attributes of the Course model."""      
        self.assertEqual(self.course.course_id, 'ex301')
        self.assertEqual(self.course.description, 'Example course description')
        self.assertEqual(self.course.level, 'B')

class EnrollmentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='2000-01-01',
            email='john.doe@example.com',
            cpf='38337731036',
            cell_phone_number='86 99999-9999'
        )
        
        self.course = Course.objects.create(
            course_id='ex301',
            description='Example course description',
            level='B'
        )
        
        self.enrollment = Enrollment.objects.create(
            student = self.student,
            course = self.course,
            shift = 'M'
        )
    
    def test_enrollment_creation(self):
        """
        The test verifies attributes of the Enrollment model.
        """      
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.course, self.course)
        self.assertEqual(self.enrollment.shift, 'M')