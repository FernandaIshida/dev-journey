from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentStudentsListSerializer, EnrollmentCoursesListSerializer, StudentSerializerV2
from school.throttles import EnrollmentAnonThrottle

from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle

class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet Description:
    - Endpoint for CRUD operations on students.

    Ordering fields:
    - name: allows ordering results by name.

    Search fields:
    - name: allows searching results by name.
    - cpf: allows searching results by CPF.

    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE

    Serializer Class:
    - StudentSerializer: used for data serialization and deserialization.
    - If the API version is 'v2', StudentSerializerV2 is used.
    """
    queryset = Student.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['first_name']
    search_fields = ['first_name', 'last_name', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet Description:
    - Endpoint for CRUD operations on courses.
    
    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet Description:
    - Endpoint for CRUD operations on enrollments.
    
    Allowed HTTP Methods:
    - GET, POST
    
    Throttling:
    - UserRateThrottle: applies user-based rate limiting.
    - EnrollmentAnonThrottle: applies custom anonymous user rate limiting.
    """
    queryset = Enrollment.objects.all().order_by('id')
    serializer_class = EnrollmentSerializer
    throttle_classes = [UserRateThrottle, EnrollmentAnonThrottle]
    http_method_names = ['get', 'post']

class EnrollmentStudentsList(generics.ListAPIView):
    """
    View description:
    - Lists all enrollments for a specific student based on the student's ID.
    Parameters:
    - pk(int): primary key of the object. Must be an integer.
    """
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id = self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = EnrollmentStudentsListSerializer

class EnrollmentCoursesList(generics.ListAPIView):
    """
    View description:
    - Lists all enrollments for a specific course based on the course's ID.
    Parameters:
    - pk(int): primary key of the object. Must be an integer.
    """
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id = self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = EnrollmentCoursesListSerializer

