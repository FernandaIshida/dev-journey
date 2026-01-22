# week-1-django-rest

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-%2358a5f0)

A well-structured REST API for managing school resources, implemented using Django and Django REST Framework.  
This project demonstrates clean architecture, organized app structure, and application of best practices in API development.

---

## Overview

The API provides endpoints to manage core school entities including **Students**, **Courses**, and **Enrollments**.  
The project follows Django conventions with a dedicated app for models, serializers, and views, as well as a clean project configuration.

Key highlights:

- Organized Django app structure with separation of concerns
- Use of DRF ViewSets and Routers for scalable REST endpoints
- Proper model relationships, validations, and serializers
- Prepared for extension and integration with authentication/permissions

---

## Project Structure

- **school/** – Main application containing models, serializers, views, and tests
- **setup/** – Project configuration (settings, URLs, WSGI/ASGI)
- **manage.py** – Django management utility
- **requirements.txt** – Project dependencies
- **db.sqlite3** – SQLite database for development

---

```mermaid
graph TD
    A[week-1-django-rest]

    A --> B[school]
    B --> B1[models.py]
    B --> B2[serializers.py]
    B --> B3[views.py]
    B --> B4[admin.py]
    B --> B5[tests.py]
    B --> B6[apps.py]

    A --> C[setup]
    C --> C1[settings.py]
    C --> C2[urls.py]
    C --> C3[asgi.py]
    C --> C4[wsgi.py]

    A --> D[manage.py]
    A --> E[requirements.txt]
    A --> F[db.sqlite3]
```

---

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/FernandaIshida/dev-journey.git
   cd dev-journey/week-1-django-rest

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Apply migrations:
   ```bash
    python manage.py migrate

4. Run the development server:
   ```bash
   python manage.py runserver

Visit: http://localhost:8000/

| Method    | Endpoint          | Description              |
| --------- | ----------------- | ------------------------ |
| GET       | `/students/`      | List all students        |
| POST      | `/students/`      | Create a new student     |
| GET       | `/students/<id>/` | Retrieve a student by ID |
| PUT/PATCH | `/students/<id>/` | Update student data      |
| DELETE    | `/students/<id>/` | Remove a student         |
| GET       | `/courses/`       | List all courses         |
| POST      | `/courses/`       | Create a new course      |
| GET       | `/courses/<id>/`  | Retrieve a course by ID  |
| PUT/PATCH | `/courses/<id>/`  | Update course data       |
| DELETE    | `/courses/<id>/`  | Remove a course          |

## Contributing

This project is maintained professionally and open to contributions via **issues** or **pull requests** .
Please follow the project conventions when extending models or API functionality.

## License

MIT License
