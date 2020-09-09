from django.shortcuts import render
from django.contrib import admin

from .models import Headstrait
from .models import A_1_Salasar
from .models import IBM
from .models import finalinfosys
from .models import finallistinfosys
from .models import lti12result
from .models import cap20nov
from .models import lti28nov
from .models import cap8jan
from .models import virt11mar
from .models import web29apr

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# from django.core.mail import EmailMessage
import csv
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.admin.utils import label_for_field



def download_csv(modeladmin, request, queryset):
    if not request.user.is_staff:#to check user authentication
        raise PermissionDenied
    opts = queryset.model._meta#to get all metadata
    response = HttpResponse()
    # force download
    response['Content-Disposition'] = f'attachment;filename=db.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field, None) for field in field_names])
    return response


def webinar(request):
    if request.method == 'GET':
        return render(request, 'tpo/Webinar.html')

    if request.method == 'POST':
        pyfname = request.POST['Student_Name']
        pysname = request.POST['Student_Name2']
        pymob = request.POST['Mobile Number']#[0:10]
        pyemail = request.POST['Email']#[0:30]
        pyemail2 = request.POST['Emaill']
        # pyclgname = request.POST['College_Name']#[0:40]
        pyorg = request.POST['Organization']
        pycity = request.POST['City']
        pystream = request.POST['Stream']
        # pyref = request.POST['Referral']
        # pyslot = request.POST['Slot']

        if web29apr.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/webfailure.html')
        if web29apr.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/webfailure.html')
        if pyemail != pyemail2:
            messages.error(request, f"Emails do not match")
            return render(request, 'tpo/webfailure.html')

        data2 = web29apr(name=pyfname, lastname=pysname, number2=pymob, email=pyemail, clg_name=pyorg, city=pycity, qualification=pystream)
        data2.save()
        messages.success(request, "Successfully registered.")
        return render(request, 'tpo/Webinar.html')

def email(pyemail):
    subject = 'Thank you for registering on our Job4U'
    message = 'Further details will be emailed to you soon.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [pyemail,]
    send_mail(subject, message, email_from, recipient_list)






# ----------------- Databases -------------------------------------


def a_1_Salasardb(request):
	studentdb = A_1_Salasar.objects.all()
	count = A_1_Salasar.objects.all().count()
	count2 = A_1_Salasar.objects.filter(confirmation='1').count()
	apsitcount = A_1_Salasar.objects.filter(clg_name='A. P. Shah institute of technology').count()
	apsitconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='A. P. Shah institute of technology').count()
	xavconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='Xavier Institute of Engineering').count()
	newhorconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='New horizon institute of technology and management').count()
	ternaconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='Terna engineering college').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2,'apsitcount':apsitcount,'apsitconf':apsitconf,'xavconf':xavconf,'newhorconf':newhorconf,'ternaconf':ternaconf})

def returndb(request, db):
    studentdb = db.objects.all()
	count = db.objects.all().count()
	count2 = db.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})


def web1005db(request):
    studentdb = web29apr.objects.all()
    count = web29apr.objects.all().count()
    if request.method == 'POST' and 'csv' in request.POST:
        return download_csv(admin, request, studentdb)
    return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count})
    # if request.method == 'POST' and 'csv' in request.POST:
    #     studentdb = web29apr.objects.all()
    #     return download_csv(admin, request, studentdb)

def return_lti_csv(request, studentdb):
    if request.method == 'POST' and 'csv' in request.POST:
        return download_csv(admin, request, studentdb)

def virt1103db(request):
    studentdb = virt11mar.objects.all()
    count = virt11mar.objects.all().count()
    count2 = virt11mar.objects.filter(confirmation='1').count()
    if request.method == 'POST' and 'csv' in request.POST:
        return download_csv(admin, request, studentdb)
    return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})




# ----------------- Databases end -------------------------------------





def admin_panel(request):
	return render(request, 'tpo/admin_panel.html')


# ibm function is template function build page for on campus attendence
# ibm.html is template with all necessary fields
def ibm(request):
    if request.method == 'GET':
        return render(request, 'tpo/ibm.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyfname = request.POST['Student_Name']
        # pysname = request.POST['Student_Name2']
        pymob = request.POST['Mobile Number']#[0:10]
        pyemail = request.POST['Email']#[0:30]
        pyclgname = request.POST['College_Name']#[0:40]
        # pybranch = request.POST['Branch']
        # pydeg = request.POST['Deg_type']
        # pyyear = request.POST['Passyear']
        # pyref = request.POST['Referral']
        pyslot = request.POST['Slot']

        if virt11mar.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/ibm.html')
        if virt11mar.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/ibm.html')

        data2 = virt11mar(name=pyfname, number2=pymob, email=pyemail, clg_name=pyclgname,slot=pyslot, confirmation=1)
        data2.save()
        messages.success(request, "Successfully registered.")
        return render(request, 'tpo/ibm.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        # pyemail = request.POST['confemail']
        if (virt11mar.objects.filter(number2=pymob2).exists()) and pymob2!="":
            virt11mar.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed")
            return render(request, 'tpo/ibm.html')

        else:
            messages.error(request, f"Not registered")
            return render(request, 'tpo/ibm.html')



def index(request):
	return render(request, 'tpo/index.html')


def administrator(request):
	return render(request, 'tpo/administrator.html')

def returnresult(request, db):
    studentdb = db.objects.all()
    return render(request,'tpo/ltiresult.html', {'studentdb':studentdb})
