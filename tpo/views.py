from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Google
from .models import Headstrait
from .models import Amazon
from .models import A_1_Salasar
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
import csv
import os


if not os.path.isfile('./A_1_Salasar.csv'):
	with open('A_1_Salasar.csv', 'w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])

if not os.path.isfile('./Google.csv'):
	with open('Google.csv', 'w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])

if not os.path.isfile('./Headstrait.csv'):
	with open('Headstrait.csv', 'w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])

if not os.path.isfile('./Amazon.csv'):
	with open('Amazon.csv', 'w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])


def email(pyemail):
    subject = 'Thank you for registering on our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [pyemail,]
    send_mail(subject, message, email_from, recipient_list)


def administrator(request):
	return render(request, 'tpo/administrator.html')

def index(request):
	'''if request.method == 'POST':
	company_name = request.POST['NameofCompany']
	sender_name = request.POST['NameofSender']
	pydate = '''
	return render(request, 'tpo/index.html')


def amazondb(request):
	studentdb = Amazon.objects.all()
	count = Amazon.objects.all().count()
	count2 = Amazon.objects.filter(confirmation='1').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2})

def googledb(request):
	studentdb = Google.objects.all()
	count = Google.objects.all().count()
	count2 = Google.objects.filter(confirmation='1').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2})

def a_1_Salasardb(request):
	studentdb = A_1_Salasar.objects.all()
	count = A_1_Salasar.objects.all().count()
	count2 = A_1_Salasar.objects.filter(confirmation='1').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2})

def headstraitdb(request):
	studentdb = Headstrait.objects.all()
	count = Headstrait.objects.all().count()
	count2 = Headstrait.objects.filter(confirmation='1').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2})


def admin_panel(request):
	if request.method == 'POST' and 'email_amazon_db' in request.POST:
		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
		msg.content_subtype = "html"
		msg.attach_file('Amazon.csv')
		msg.send()
		messages.success(request, "Emailed Database.")
	#return render(request, 'tpo/admin_panel.html')

	elif request.method == 'POST' and 'email_google_db' in request.POST:
		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
		msg.content_subtype = "html"
		msg.attach_file('Google.csv')
		msg.send()
		messages.success(request, "Emailed Database.")
	#return render(request, 'tpo/admin_panel.html')

	elif request.method == 'POST' and 'a_1_Salasar_db' in request.POST:
		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['anujssmishra@gmail.com','vedantmh@gmail.com'])
		msg.content_subtype = "html"
		msg.attach_file('A_1_Salasar.csv')
		msg.send()
		messages.success(request, "Emailed Database.")

	elif request.method == 'POST' and 'email_headstrait_db' in request.POST:
		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
		msg.content_subtype = "html"
		msg.attach_file('Headstrait.csv')
		msg.send()
		messages.success(request, "Emailed Database.")
	return render(request, 'tpo/admin_panel.html')


def google(request):
    if request.method == 'GET':
        return render(request, 'tpo/google.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyname = request.POST['Student_Name']
        pymob = request.POST['Mobile Number']
        pyemail = request.POST['Email']
        pyclgname = request.POST['College_Name']
        pybranch = request.POST['Branch']
        pyslot = request.POST['Slot']

        if Google.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/google.html')
        if Google.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/google.html')

        data2 = Google(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, slot=pyslot)
        data2.save()
        messages.success(request, "Successfully registered.")
        with open('Google.csv', 'a', newline='') as csvfile:
    	    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    	    filewriter.writerow([pyname, pymob,pyemail,pyclgname,pybranch,pyslot])

        email(pyemail)
        return render(request, 'tpo/google.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        if Google.objects.filter(number2=pymob2).exists():
            Google.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed for {pymob2}")
    	    #send_mail('All the best for drive', 'Your ', email_from, recipient_list)
            return render(request, 'tpo/google.html')
        else:
            messages.error(request, f"The number {pymob2} is not registered")
            return render(request, 'tpo/google.html')

def headstrait(request):
    if request.method == 'GET':
        return render(request, 'tpo/headstrait.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyname = request.POST['Student_Name']
        pymob = request.POST['Mobile Number']
        pyemail = request.POST['Email']
        pyclgname = request.POST['College_Name']
        pybranch = request.POST['Branch']
        pyslot = request.POST['Slot']

        if Headstrait.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/headstrait.html')
        if Headstrait.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/headstrait.html')

        data2 = Headstrait(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, slot=pyslot)
        data2.save()
        messages.success(request, "Successfully registered.")
        with open('Headstrait.csv', 'a', newline='') as csvfile:
    	    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    	    filewriter.writerow([pyname, pymob,pyemail,pyclgname,pybranch,pyslot])

        email(pyemail)
        return render(request, 'tpo/headstrait.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        if Headstrait.objects.filter(number2=pymob2).exists():
            Headstrait.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed for {pymob2}")
    	    #send_mail('All the best for drive', 'Your ', email_from, recipient_list)
            return render(request, 'tpo/headstrait.html')
        else:
            messages.error(request, f"The number {pymob2} is not registered")
            return render(request, 'tpo/headstrait.html')

def amazon(request):
    if request.method == 'GET':
        return render(request, 'tpo/amazon.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyname = request.POST['Student_Name']
        pymob = request.POST['Mobile Number']
        pyemail = request.POST['Email']
        pyclgname = request.POST['College_Name']
        pybranch = request.POST['Branch']
        pyslot = request.POST['Slot']

        if Amazon.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/amazon.html')
        if Amazon.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/amazon.html')

        data2 = Amazon(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, slot=pyslot)
        data2.save()
        messages.success(request, "Successfully registered.")
        with open('Amazon.csv', 'a', newline='') as csvfile:
    	    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    	    filewriter.writerow([pyname, pymob,pyemail,pyclgname,pybranch,pyslot])

        email(pyemail)
        return render(request, 'tpo/amazon.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        if Amazon.objects.filter(number2=pymob2).exists():
            Amazon.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed for {pymob2}")
    	    #send_mail('All the best for drive', 'Your ', email_from, recipient_list)
            return render(request, 'tpo/amazon.html')
        else:
            messages.error(request, f"The number {pymob2} is not registered")
            return render(request, 'tpo/amazon.html')

def a_1_Salasar(request):
    if request.method == 'GET':
        return render(request, 'tpo/a_1_Salasar.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyname = request.POST['Student_Name']#[0:30]
        pymob = request.POST['Mobile Number']#[0:10]
        pyemail = request.POST['Email']#[0:30]
        pyclgname = request.POST['College_Name']#[0:40]
        pybranch = request.POST['Branch']#[0:20]
        pyslot = request.POST['Slot']#[0:10]

        if A_1_Salasar.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/a_1_Salasar.html')
        if A_1_Salasar.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/a_1_Salasar.html')

        data2 = A_1_Salasar(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, slot=pyslot)
        data2.save()
        messages.success(request, "Successfully registered.")
        with open('A_1_Salasar.csv', 'a', newline='') as csvfile:
    	    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    	    filewriter.writerow([pyname, pymob,pyemail,pyclgname,pybranch,pyslot])

        email(pyemail)
        return render(request, 'tpo/a_1_Salasar.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        if A_1_Salasar.objects.filter(number2=pymob2).exists():
            A_1_Salasar.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed for {pymob2}")
            return render(request, 'tpo/a_1_Salasar.html')
        else:
            messages.error(request, f"The number {pymob2} is not registered")
            return render(request, 'tpo/a_1_Salasar.html')
