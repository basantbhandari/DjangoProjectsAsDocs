from django.db import models


# Create your models here.
class Student(models.Model):
    """Model definition for Student."""
    name = models.CharField(max_length=70)
    roll = models.IntegerField(null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    passdate = models.DateField()
    admdatetime = models.DateTimeField()
