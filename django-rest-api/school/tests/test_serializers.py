from django.test import TestCase
from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer

class StudentSerializerTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name='John',
            last_name='Doe',
            date_of_birth='2000-01-01',
            email='john.doe@example.com',
            cpf='38337731036',
            cell_phone_number='86 99999-9999'
        )
        self.student_serializer = StudentSerializer(instance = self.student)

    def test_student_serializer(self):
        """
        The test verifies the fields of the StudentSerializer.
        """
        data = self.student_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'first_name', 'last_name', 'date_of_birth', 'email', 'cpf', 'cell_phone_number']))

    def test_student_serializer_content(self):
        """
        The test verifies the content of the fields of the StudentSerializer.
        """
        data = self.student_serializer.data
        self.assertEqual(data['first_name'], 'John')
        self.assertEqual(data['last_name'], 'Doe')
        self.assertEqual(data['date_of_birth'], '2000-01-01')
        self.assertEqual(data['email'], 'john.doe@example.com')
        self.assertEqual(data['cpf'], '38337731036')
        self.assertEqual(data['cell_phone_number'], '86 99999-9999')

class CourseSerializerTestCase(TestCase):
    def setUp(self):
        self.course = Course(
            course_id='ex301',
            description='Example course description',
            level='B')
        self.course_serializer = CourseSerializer(instance = self.course)

    def test_course_serializer(self):
        """
        The test verifies the fields of the CourseSerializer.
        """
        data = self.course_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'course_id', 'description', 'level']))

    def test_course_serializer_content(self):
        """
        The test verifies the content of the fields of the CourseSerializer.
        """
        data = self.course_serializer.data
        self.assertEqual(data['course_id'], 'ex301')
        self.assertEqual(data['description'], 'Example course description')
        self.assertEqual(data['level'], 'B')    

class EnrollmentSerializertestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name='John',
            last_name='Doe',
            date_of_birth='2000-01-01',
            email='john.doe@example.com',
            cpf='38337731036',
            cell_phone_number='86 99999-9999'
        )
        
        self.course = Course(
            course_id='ex301',
            description='Example course description',
            level='B'
        )
        
        self.enrollment = Enrollment(
            student = self.student,
            course = self.course,
            shift = 'M'
        )
        self.enrollment_serializer = EnrollmentSerializer(instance = self.enrollment)

    def test_enrollment_serializer(self):
        """
        The test verifies the fields of the EnrollmentSerializer.
        """
        data = self.enrollment_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'student', 'course', 'shift']))

    def test_enrollment_serializer_content(self):
        """
        The test verifies the content of the fields of the EnrollmentSerializer.
        """
        data = self.enrollment_serializer.data
        self.assertEqual(data['student'], self.student.id)
        self.assertEqual(data['course'], self.course.id)
        self.assertEqual(data['shift'], 'M')