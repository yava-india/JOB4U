from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator, MaxValueValidator


class Google(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=30)
    # number2 = models.BigIntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)])
    number2 = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    clg_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    slot = models.CharField(max_length=15, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

class Headstrait(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=30)
    # number2 = models.BigIntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)])
    number2 = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    clg_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    slot = models.CharField(max_length=15, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

class Amazon(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=30)
    # number2 = models.BigIntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)])
    number2 = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    clg_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    slot = models.CharField(max_length=15, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

class A_1_Salasar(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=60)
    # number2 = models.BigIntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)])
    number2 = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    clg_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    reporting_time = models.CharField(max_length=50, blank=True)
    profile = models.CharField(max_length=50, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)
