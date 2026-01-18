from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        students = {
            'id': '1',
            'name': 'John Doe'
        }
        return JsonResponse(students)