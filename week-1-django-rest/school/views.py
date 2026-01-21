from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentStudentsListSerializer, EnrollmentCoursesListSerializer

from rest_framework import viewsets, generics

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentStudentsList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentStudentsListSerializer

class EnrollmentCoursesList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentCoursesListSerializer

