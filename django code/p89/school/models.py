from django.db import models

# Create your models here.


class Student(models.Model):
    """Model definition for Student."""

    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()


class Teacher(models.Model):
    """Model definition for Teacher."""

    name = models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
