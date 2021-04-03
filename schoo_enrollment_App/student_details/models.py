from datetime import date

from django.core.validators import BaseValidator
from django.db import models

# Create your models here.
from django.utils.deconstruct import deconstructible

Classes_CHOICES = (
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True, blank=True, null=True)
    class_opted = models.CharField(
        max_length=20,
        choices=Classes_CHOICES,
        default='5'
    )
    marks = models.FloatField(blank=True, null=True)
    date_enrolled = models.DateTimeField(auto_now_add=True)


