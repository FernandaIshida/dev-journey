from rest_framework import serializers
from school.models import Student, Course,Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentStudentsListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    shift = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'shift']
    def get_shift(self, obj):
        return obj.get_shift_display()
    
class EnrollmentCoursesListSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['student_name']
    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"


