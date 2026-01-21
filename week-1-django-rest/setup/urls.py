from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, EnrollmentStudentsList, EnrollmentCoursesList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('enrollments', EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', EnrollmentStudentsList.as_view()),
    path('courses/<int:pk>/enrollments/', EnrollmentCoursesList.as_view()),
]