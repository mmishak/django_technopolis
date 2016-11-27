from django.contrib import admin

# Register your models here.

from .models import Student, Cource

admin.site.register(Student)
admin.site.register(Cource)
