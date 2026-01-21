from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    date_of_birth = models.DateField()
    email = models.EmailField(blank = False)
    cpf = models.CharField(max_length = 11)
    phone_number = models.CharField(max_length = 14)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    
    course_id = models.CharField(max_length = 10,  unique = True)
    description = models.CharField(max_length = 255, blank = False)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.course_id
    
class Enrollment(models.Model):
    SHIFT = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening')
    )
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    shift = models.CharField(max_length = 1, choices = SHIFT, blank = False, null = False, default = 'M')
    



