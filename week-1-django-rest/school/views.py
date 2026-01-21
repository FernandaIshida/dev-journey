from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentStudentsListSerializer, EnrollmentCoursesListSerializer

from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentStudentsList(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentStudentsListSerializer

class EnrollmentCoursesList(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentCoursesListSerializer

