from django.conf.urls import url

from . import views

app_name = 'practice'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.StudentCreate.as_view(), name='create'),
    # ex: /practice/5/
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.StudentUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='delete'),
    # ex: /practice/5/courses/
    url(r'^(?P<pk>[0-9]+)/courses/$', views.CoursesView.as_view(), name='courses'),
    url(r'^(?P<student_id>[0-9]+)/$', views.choose, name='choose'),
]