from django.conf.urls import url

from . import views

app_name = 'practice'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /practice/5/
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    # ex: /practice/5/courses/
    url(r'^(?P<pk>[0-9]+)/courses/$', views.CoursesView.as_view(), name='courses'),
    url(r'^(?P<student_id>[0-9]+)/$', views.choose, name='choose'),
]