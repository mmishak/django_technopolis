from django.conf.urls import url

from . import views

app_name = 'practice'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /practice/5/
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /practice/5/courses/
    url(r'^(?P<student_id>[0-9]+)/courses/$', views.courses, name='courses'),
    url(r'^(?P<student_id>[0-9]+)/choose/$', views.choose, name='choose'),
]