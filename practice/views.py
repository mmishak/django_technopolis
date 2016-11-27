from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

from practice.models import Student


def index(request):
    students_list = Student.objects.order_by('name')
    context = {'students_list': students_list}
    return render(request, "practice/index.html", context)


def detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Студент с id = " + student_id + " не найден")
    return render(request, 'practice/detail.html', {'student': student})


def cources(request, student_id):
    response = "Это страница с курсами на которые записан студент: %s"
    return HttpResponse(response % student_id)
