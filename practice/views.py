
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from django.urls import reverse

from practice.models import Student, Cource, StudentCources



def index(request):
    students_list = Student.objects.order_by('name')
    context = {'students_list': students_list}
    return render(request, "practice/index.html", context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    cources_list = Cource.objects.order_by('name')
    return render(request, 'practice/detail.html', {'student': student, 'cources_list': cources_list})


def choose(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        selected_cource = Cource.objects.get(pk=request.POST['cource'])
    except (KeyError, Cource.DoesNotExist):
        return render(request, 'practice/detail.html', {
            'student': student,
            'error_message': "Вы не выбрали курс",
        })
    else:
        if StudentCources.objects.filter(student=student, cource=selected_cource):
            return render(request, 'practice/detail.html', {
                'student': student,
                'error_message': "Студент уже записан на этот курс",
            })

        student_cource = StudentCources(student=student, cource=selected_cource)
        student_cource.save()

        return HttpResponseRedirect(reverse('practice:cources', args=(student.id,)))


def cources(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student_cources_list = StudentCources.objects.all();
    cource_list = []
    for item in student_cources_list:
        if item.student.id == student.id:
            cource_list.append(Cource.objects.get(pk=item.cource.id))

    return render(request, 'practice/cources.html', {
        'student': student,
        'cource_list': cource_list,
    })
