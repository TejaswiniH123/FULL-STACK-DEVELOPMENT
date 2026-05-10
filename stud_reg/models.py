from django.db import models


class Course(models.Model):
    coursecode = models.CharField(max_length=10)
    coursename = models.CharField(max_length=50)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.coursecode} - {self.coursename}"


class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    sem = models.IntegerField()

    enrollment = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.usn} - {self.name}"