from django.conf.urls import url

from . import views

app_name = 'practice'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /practice/5/
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /practice/5/cources/
    url(r'^(?P<student_id>[0-9]+)/cources/$', views.cources, name='cources'),
    url(r'^(?P<student_id>[0-9]+)/choose/$', views.choose, name='choose'),
]