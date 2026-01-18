from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
