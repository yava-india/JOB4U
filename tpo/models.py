from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    name = models.CharField(max_length=30, blank=False)
    number2 = models.BigIntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)], unique=True, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    clg_name = models.CharField(max_length=100, blank=False)
    branch = models.CharField(max_length=40)
    slot = models.CharField(max_length=15)
