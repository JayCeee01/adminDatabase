# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    section = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
