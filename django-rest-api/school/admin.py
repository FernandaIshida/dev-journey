from django.contrib import admin
from .models import Student, Course, Enrollment

class Students(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'email', 'cpf', 'cell_phone_number',)
    list_display_links = ('id', 'first_name', 'last_name',)
    list_per_page = 20
    search_fields = ('first_name', 'cpf')
    ordering = ('first_name',)

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'description', 'level',)
    list_display_links = ('id', 'course_id',)
    search_fields = ('course_id',)

admin.site.register(Course, Courses)

class Enrollments(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'shift',)
    list_display_links = ('id',)

admin.site.register(Enrollment, Enrollments)
