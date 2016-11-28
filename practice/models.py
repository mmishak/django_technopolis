from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.family


class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StudentCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
