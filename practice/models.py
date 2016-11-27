from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    def __str__(self):
        return self.name + " " + self.family

class Cource(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class StudentCources(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE)


