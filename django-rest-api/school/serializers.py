from rest_framework import serializers
from school.models import Student, Course,Enrollment
from school.validators import invalid_cpf, invalid_first_name, invalid_last_name, invalid_cell_phone_number

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if invalid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'The CPF must have a valid value!'})
        if invalid_first_name(data['first_name']):
            raise serializers.ValidationError({'first_name':'The name must contain only letters!'})
        if invalid_last_name(data['last_name']):
            raise serializers.ValidationError({'last_name':'The last name must contain only letters!'})
        if invalid_cell_phone_number(data['cell_phone_number']):
            raise serializers.ValidationError({'cell_phone_number':'The cell phone number must follow the format: 86 99999-9999 (respecting dashes and spaces).'})
        return data

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
    
class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'cell_phone_number']    


