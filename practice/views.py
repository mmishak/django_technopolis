from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from django.urls import reverse

from practice.models import Student, Course, StudentCourses


def choose(request, student_id):
    course_list = Course.objects.all()
    student = get_object_or_404(Student, pk=student_id)
    try:
        selected_course = Course.objects.get(pk=request.POST['course'])
    except (KeyError, Course.DoesNotExist):
        return render(request, 'practice/detail.html', {
            'student': student,
            'error_message': "Вы не выбрали курс",
            'course_list': course_list,
        })
    else:
        if StudentCourses.objects.filter(student=student, course=selected_course):
            return render(request, 'practice/detail.html', {
                'student': student,
                'error_message': "Студент уже записан на этот курс",
                'course_list': course_list,
            })

        student_course = StudentCourses(student=student, course=selected_course)
        student_course.save()

        return HttpResponseRedirect(reverse('practice:courses', args=(student.id,)))


class IndexView(generic.ListView):
    template_name = 'practice/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Student
    template_name = 'practice/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the courses
        context['course_list'] = Course.objects.order_by('name')
        return context


class CoursesView(generic.DetailView):
    model = Student
    template_name = 'practice/courses.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesView, self).get_context_data(**kwargs)

        context['course_list'] = self.get_course_list()
        return context

    def get_course_list(self):
        student_courses_list = StudentCourses.objects.all()

        course_list = []
        for item in student_courses_list:
            if item.student.id == self.object.id:
                course_list.append(Course.objects.get(pk=item.course.id))

        return course_list
