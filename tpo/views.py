from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    if request.method == 'GET':
        return render(request, 'tpo/home.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyname = request.POST['Student_Name']
        pymob = request.POST['Mobile Number']
        pyemail = request.POST['Email']
        pyclgname = request.POST['College_Name']
        pybranch = request.POST['Branch']
        pyslot = request.POST['Slot']

        if Student.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/home.html')
        if Student.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/home.html')

        data2 = Student(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, slot=pyslot)
        data2.save()
        messages.success(request, "Successfully registered.")
        # email(request)
        return render(request, 'tpo/home.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        if Student.objects.filter(number2=pymob2).exists():
            Student.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed for {pymob2}")
            return render(request, 'tpo/home.html')
        else:
            messages.error(request, f"The number {pymob2} is not registered")
            return render(request, 'tpo/home.html')


def email(request):
    subject = 'Thank you for registering on our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['pyemail']
    send_mail(subject, message, email_from, recipient_list)


def about(request):
    return render(request, 'tpo/about.html')
