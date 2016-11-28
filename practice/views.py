
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from django.urls import reverse

from practice.models import Student, Course, StudentCourses


def index(request):
    students_list = Student.objects.order_by('name')
    context = {'students_list': students_list}
    return render(request, "practice/index.html", context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses_list = Course.objects.order_by('name')
    return render(request, 'practice/detail.html', {'student': student, 'courses_list': courses_list})


def choose(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        selected_course = Course.objects.get(pk=request.POST['course'])
    except (KeyError, Course.DoesNotExist):
        return render(request, 'practice/detail.html', {
            'student': student,
            'error_message': "Вы не выбрали курс",
        })
    else:
        if StudentCourses.objects.filter(student=student, course=selected_course):
            return render(request, 'practice/detail.html', {
                'student': student,
                'error_message': "Студент уже записан на этот курс",
            })

        student_course = StudentCourses(student=student, course=selected_course)
        student_course.save()

        return HttpResponseRedirect(reverse('practice:courses', args=(student.id,)))


def courses(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student_courses_list = StudentCourses.objects.all();
    course_list = []
    for item in student_courses_list:
        if item.student.id == student.id:
            course_list.append(Course.objects.get(pk=item.course.id))

    return render(request, 'practice/courses.html', {
        'student': student,
        'course_list': course_list,
    })
