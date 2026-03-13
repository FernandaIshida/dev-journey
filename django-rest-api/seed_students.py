import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from school.models import Student

def seed_students(number_of_students):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(number_of_students):
        cpf = CPF()
        first_name = fake.name()
        last_name = fake.last_name()
        email = '{}@{}'.format(first_name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=30)  # Generate a random date of birth between 18 and 30 years old
        cell_phone_number = "{} 9{}-{}".format(random.randrange(10, 89), random.randrange(4000, 9999), random.randrange(4000, 9999))
        p = Student(first_name=first_name, last_name=last_name, email=email, cpf=cpf, date_of_birth=date_of_birth, cell_phone_number=cell_phone_number)
        p.save()

seed_students(50)