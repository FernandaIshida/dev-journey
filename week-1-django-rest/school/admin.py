from django.contrib import admin
from .models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'email', 'cpf', 'phone_number',)
    list_display_links = ('id', 'first_name', 'last_name',)
    list_per_page = 20
    search_fields = ('first_name',)

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'description', 'level',)
    list_display_links = ('id', 'course_id',)
    search_fields = ('course_id',)

admin.site.register(Course, Courses)
