from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .models import Student
# Create your views here.

def test_portal(req):
    return HttpResponse("Welcome to your Portal")

def portal(req):
    return HttpResponse("Welcome")

def all_students_json(request):
    students = Student.objects.all()
    # serialize_students = serialize('json',students)
    # return JsonResponse(serialize_students, safe=False)
    student_names = [student.name for student in students]
    data = {'names': student_names}

    return JsonResponse(data, safe=False)

def base_view(request):
    return render(request, 'html/base.html')

# def home(request):
#     return render(request, 'html/home.html')
