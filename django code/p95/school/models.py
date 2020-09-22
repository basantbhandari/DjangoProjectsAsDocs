from django.db import models

# Create your models here.


class commonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class Student(commonInfo):
    fees = models.IntegerField()


class Teacher(commonInfo):
    salary = models.IntegerField()


class Contractor(commonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()
