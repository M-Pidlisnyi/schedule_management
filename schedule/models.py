from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=50)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="teachers")
    

class Group(models.Model):
    year = models.PositiveIntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])#7
    code = models.CharField(max_length=1)#Б
    

    def __str__(self):
        return f"{self.year}-{self.code}"#7-Б
    
class Student(models.Model):
    name = models.CharField(max_length=50)

    group  = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    time = models.TimeField()


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    value = models.PositiveIntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    