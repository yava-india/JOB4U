from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator, MaxValueValidator


class swab12dec(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    number2 = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100, blank=True)
    # degtype = models.CharField(max_length=15)
    # passyear = models.CharField(max_length=20)
    branch = models.CharField(max_length=40, blank=True)
    # slot = models.CharField(max_length=40, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

class lti28nov(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    number2 = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100)
    # degtype = models.CharField(max_length=15)
    # passyear = models.CharField(max_length=20)
    slot = models.CharField(max_length=40)
    refid = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)

class bit9nov(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    number2 = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100)
    # degtype = models.CharField(max_length=15)
    # passyear = models.CharField(max_length=20)
    slot = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)

class cap20nov(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    number2 = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100)
    # degtype = models.CharField(max_length=15)
    # passyear = models.CharField(max_length=20)
    slot = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)

class infosys15nov(models.Model):
    firstname = models.CharField(max_length=60, blank=True)
    lastname = models.CharField(max_length=60, blank=True)
    number2 = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50, blank=True)
    clg_name = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=40, blank=True)
    # slot = models.CharField(max_length=40, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

class lti20nov(models.Model):
    slot = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    clg_name = models.CharField(max_length=100)
    number2 = models.CharField(max_length=100)
    degtype = models.CharField(max_length=15)
    branch = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)

class lti12result(models.Model):
    name = models.CharField(max_length=50)
    clg_name = models.CharField(max_length=100)

class virtusa(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    clg_name = models.CharField(max_length=100)
    number2 = models.CharField(max_length=100)
    degtype = models.CharField(max_length=15)
    passyear = models.CharField(max_length=20)
    branch = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)

class zycus(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    number2 = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    clg_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)


class finalinfosys(models.Model):
    clg_name = models.CharField(max_length=120)
    count = models.CharField(max_length=40)

class finallistinfosys(models.Model):
    firstname = models.CharField(max_length=60)
    middlename = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    clg_name = models.CharField(max_length=120)
    branch = models.CharField(max_length=40)


class IbmResult(models.Model):
    name = models.CharField(max_length=60)
    # lastname = models.CharField(max_length=60)
    clg_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=40)

class Infosys15Result(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60, blank=True)
    clg_name = models.CharField(max_length=120)

class Infosys16Result(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60, blank=True)
    clg_name = models.CharField(max_length=120)

class infosys15oct(models.Model):
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    number2 = models.CharField(max_length=100)
    #  = models.CharField(max_length=40)
    # typedegre= models.CharField(max_length=40)
    # aggpointer = models.CharField(max_length=40)
    clg_name = models.CharField(max_length=100)
    slot = models.CharField(max_length=50, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

class infosys16oct(models.Model):
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    number2 = models.CharField(max_length=100)
    #  = models.CharField(max_length=40)
    # typedegre= models.CharField(max_length=40)
    # aggpointer = models.CharField(max_length=40)
    clg_name = models.CharField(max_length=100)
    slot = models.CharField(max_length=50, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)

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

class IBM(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=60)
    # gender = models.CharField(max_length=40)
    number2 = models.CharField(max_length=100)
    # percent10 = models.CharField(max_length=40)
    # percent12 = models.CharField(max_length=40)
    # degpassyear = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    # typedegree = models.CharField(max_length=40)
    # aggpointer = models.CharField(max_length=40)
    clg_name = models.CharField(max_length=100)
    # univname = models.CharField(max_length=70)
    # nation = models.CharField(max_length=40)
    # exp = models.CharField(max_length=100)
    # course = models.CharField(max_length=100)
    # coursecompdate = models.CharField(max_length=40)
    # reporting_time = models.CharField(max_length=50, blank=True)
    # profile = models.CharField(max_length=50, blank=True)
    confirmation = models.CharField(max_length=6, blank=True)


class IBM7oct(models.Model):
    # student_id = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=60)
    # gender = models.CharField(max_length=40)
    number2 = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    clg_name = models.CharField(max_length=100)
    confirmation = models.CharField(max_length=6, blank=True)



class Lti_23_oct(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    number2 = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=40)
    qualification = models.CharField(max_length=100)
    passingyear10 = models.CharField(max_length=40)
    percent10 = models.CharField(max_length=40)
    passingyear12 = models.CharField(max_length=40, blank=True)
    percent12 = models.CharField(max_length=40, blank=True)
    diplomapassyear = models.CharField(max_length=40, blank=True)
    diplomapercent = models.CharField(max_length=40, blank=True)
    pointer = models.CharField(max_length=40)
    degreepassyear = models.CharField(max_length=40, blank=True)
    nationality = models.CharField(max_length=40)
    confirmation = models.CharField(max_length=6, blank=True)
    tponame = models.CharField(max_length=60, blank=True)
    tponumber = models.CharField(max_length=100, blank=True)
    tpoemail = models.CharField(max_length=60, blank=True)
