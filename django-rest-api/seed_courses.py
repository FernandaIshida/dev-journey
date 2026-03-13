import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from school.models import Course

data = [
    ('CPOO1', 'Object-Oriented Python Course 01'),
    ('CPOO2', 'Object-Oriented Python Course 02'),
    ('CPOO3', 'Object-Oriented Python Course 03'),
    ('CDJ01', 'Django Course 01'),
    ('CDJ02', 'Django Course 02'),
    ('CDJ03', 'Django Course 03'),
    ('CDJ04', 'Django Course 04'),
    ('CDJ05', 'Django Course 05'),
    ('CDJRF01', 'Django REST Framework Course 01'),
    ('CDJRF02', 'Django REST Framework Course 02'),
    ('CDJRF03', 'Django REST Framework Course 03'),
    ('CDJRF04', 'Django REST Framework Course 04'),
]

levels = ['B', 'I', 'A']

def seed_courses():
    for course_id, description in data:
        level = random.choice(levels)
        Course.objects.create(course_id=course_id, description=description, level=level)

seed_courses()