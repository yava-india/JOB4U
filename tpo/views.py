from django.shortcuts import render
from .models import Google
from .models import Headstrait
from .models import Amazon
from .models import A_1_Salasar
from .models import Lti_23_oct
from .models import IBM
from .models import IbmResult
from .models import IBM7oct
from .models import infosys15oct
from .models import infosys16oct
from .models import Infosys15Result
from .models import Infosys16Result
from .models import finalinfosys
from .models import finallistinfosys
from .models import zycus
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
import csv
import os


# if not os.path.isfile('./A_1_Salasar.csv'):
# 	with open('A_1_Salasar.csv', 'w', newline='') as csvfile:
# 		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Reporting Time','Profile'])

# if not os.path.isfile('./Google.csv'):
# 	with open('Google.csv', 'w', newline='') as csvfile:
# 		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])

# if not os.path.isfile('./Headstrait.csv'):
# 	with open('Headstrait.csv', 'w', newline='') as csvfile:
# 		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])

# if not os.path.isfile('./Amazon.csv'):
# 	with open('Amazon.csv', 'w', newline='') as csvfile:
# 		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Slot'])

# if not os.path.isfile('./ibm.csv'):
# 	with open('Amazon.csv', 'w', newline='') as csvfile:
# 		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch'])



if not os.path.isfile('./lti.csv'):
	with open('lti.csv', 'w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Qualification','10th Passing Year','10th Percentage','12th Passing Year','12th Percentage','Diploma Passing Year','Diploma Percentage','Aggregate Graduation Pointer','Degree Paassing Year','Nationality','TPO Name','TPO Number','TPO Email'])



def email(pyemail):
    subject = 'Thank you for registering on our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [pyemail,]
    send_mail(subject, message, email_from, recipient_list)


def administrator(request):
	return render(request, 'tpo/administrator.html')

def thank(request):
	return render(request, 'tpo/result.html')

def Infosys(request):
    return render(request,'tpo/infosys.html')

def Infofinalresult(request):
    studentdb = finalinfosys.objects.all()
    return render(request,'tpo/infoclglist.html', {'studentdb':studentdb})

def Infofinalnameresult(request):
    studentdb = finallistinfosys.objects.all()
    return render(request,'tpo/infofinalnamelist.html', {'studentdb':studentdb})

def IBmresult(request):
    studentdb = IbmResult.objects.all()
    return render(request,'tpo/Ibmresult.html', {'studentdb':studentdb})

def INfosys15result(request):
    studentdb = Infosys15Result.objects.all()
    return render(request,'tpo/info3result.html', {'studentdb':studentdb})

def INfosys16result(request):
    studentdb = Infosys16Result.objects.all()
    # count = Infosys16Result.objects.all().count()
    return render(request,'tpo/info2result.html', {'studentdb':studentdb})

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
	apsitcount = A_1_Salasar.objects.filter(clg_name='A. P. Shah institute of technology').count()
	apsitconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='A. P. Shah institute of technology').count()
	xavconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='Xavier Institute of Engineering').count()
	newhorconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='New horizon institute of technology and management').count()
	ternaconf = A_1_Salasar.objects.filter(confirmation='1',clg_name='Terna engineering college').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2,'apsitcount':apsitcount,'apsitconf':apsitconf,'xavconf':xavconf,'newhorconf':newhorconf,'ternaconf':ternaconf})

def headstraitdb(request):
	studentdb = Headstrait.objects.all()
	count = Headstrait.objects.all().count()
	count2 = Headstrait.objects.filter(confirmation='1').count()
	return render(request, 'tpo/database.html', {'studentdb':studentdb,'count':count,'count2':count2})

def ibmdatabase(request):
	studentdb = IBM.objects.all()
	count = IBM.objects.all().count()
	count2 = IBM.objects.filter(confirmation='1').count()
	return render(request, 'tpo/ibmdatabase.html', {'studentdb':studentdb,'count':count,'count2':count2})

def info15database(request):
	studentdb = infosys15oct.objects.all()
	count = infosys15oct.objects.all().count()
	count2 = infosys15oct.objects.filter(confirmation='1').count()
	return render(request, 'tpo/inforesult.html', {'studentdb':studentdb,'count':count,'count2':count2})

def info16database(request):
	studentdb = infosys16oct.objects.all()
	count = infosys16oct.objects.all().count()
	count2 = infosys16oct.objects.filter(confirmation='1').count()
	return render(request, 'tpo/inforesult.html', {'studentdb':studentdb,'count':count,'count2':count2})

def zycusdatabase(request):
	studentdb = zycus.objects.all()
	count = zycus.objects.all().count()
	count2 = zycus.objects.filter(confirmation='1').count()
	return render(request, 'tpo/inforesult.html', {'studentdb':studentdb,'count':count,'count2':count2})

def newibmdatabase(request):
	studentdb = IBM7oct.objects.all()
	count = IBM7oct.objects.all().count()
	count2 = IBM7oct.objects.filter(confirmation='1').count()
	return render(request, 'tpo/ibmdatabase.html', {'studentdb':studentdb,'count':count,'count2':count2})

def lti_db(request):
	studentdb = Lti_23_oct.objects.all()
	count = Lti_23_oct.objects.all().count()
	return render(request, 'tpo/ltidb.html', {'studentdb': studentdb, 'count': count})



def admin_panel(request):
	if request.method == 'POST' and 'email_amazon_db' in request.POST:
		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
		msg.content_subtype = "html"
		msg.attach_file('Amazon.csv')
		msg.send()
		messages.success(request, "Emailed Database.")
	#return render(request, 'tpo/admin_panel.html')

# 	elif request.method == 'POST' and 'email_google_db' in request.POST:
# 		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
# 		msg.content_subtype = "html"
# 		msg.attach_file('Google.csv')
# 		msg.send()
# 		messages.success(request, "Emailed Database.")
# 	#return render(request, 'tpo/admin_panel.html')

# 	elif request.method == 'POST' and 'a_1_Salasar_db' in request.POST:
# 		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
# 		msg.content_subtype = "html"
# 		msg.attach_file('A_1_Salasar.csv')
# 		msg.send()
# 		messages.success(request, "Emailed Database.")

# 	elif request.method == 'POST' and 'ltiemail_db' in request.POST:
# 		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER, ['vedantmh@gmail.com','amvichare@apsit.edu.in','tpo@apsit.edu.in'])
# 		msg.content_subtype = "html"
# 		msg.attach_file('lti.csv')
# 		msg.send()
# 		messages.success(request, "Emailed Database.")

	elif request.method == 'POST' and 'email_headstrait_db' in request.POST:
		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER,['vedantmh@gmail.com'])
		msg.content_subtype = "html"
		msg.attach_file('Headstrait.csv')
		msg.send()
		messages.success(request, "Emailed Database.")
	return render(request, 'tpo/admin_panel.html')

def lti(request):
	if request.method == 'GET':
		return render(request, 'tpo/lti.html')
	if request.method == 'POST' and 'register' in request.POST:
		pyname = request.POST['Student_Name']  # [0:30]
		pymob = request.POST['Mobile Number']  # [0:10]
		pyemail = request.POST['Email']  # [0:30]
		pyclgname = request.POST['College_Name']  # [0:40]
		pybranch = request.POST['branchii']
		pyqual = request.POST['qualii']
		py10pass = request.POST['10passyear']
		py10percent = request.POST['10percent']
		py12pass = request.POST['12passyear']
		py12percent = request.POST['12percent']
		pydippass = request.POST['diplomapassyear']
		pydippercent = request.POST['diplomapercent']
		pypointer = request.POST['aggpointer']
		pynation = request.POST['nation']
		pytponame = request.POST['tpo_name']
		pytpono = request.POST['tpo_number']
		pytpoemail = request.POST['tpo_email']
		pydegreepass = 2020

# 		print(pyqual)
		if Lti_23_oct.objects.filter(number2=pymob).exists():
			messages.error(request, f"{pymob} already registered, use another")
			return render(request, 'tpo/result.html')
		if Lti_23_oct.objects.filter(email=pyemail).exists():
			messages.error(request, f"{pyemail} already registered, use another")
			return render(request, 'tpo/result.html')

		data2 = Lti_23_oct(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, qualification=pyqual, passingyear10=py10pass, percent10=py10percent, passingyear12=py12pass, percent12=py12percent, diplomapassyear=pydippass, diplomapercent=pydippercent, pointer=pypointer,degreepassyear=2020, nationality=pynation, tponame=pytponame, tponumber=pytpono, tpoemail=pytpoemail)
		data2.save()
		messages.success(request, "Successfully registered.")
		with open('lti.csv', 'a', newline='') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow([pyname, pymob, pyemail, pyclgname, pybranch, pyqual, py10pass, py10percent, py12pass, py12percent, pydippass, pydippercent, pypointer,pydegreepass, pynation, pytponame, pytpono, pytpoemail])
		return render(request, 'tpo/result.html')

def newlti(request):
    return render(request,'tpo/newlti.html')


def a_1_Salasar(request):
    if request.method == 'GET':
        return render(request, 'tpo/a_1_Salasar.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyname = request.POST['Student_Name']#[0:30]
        pymob = request.POST['Mobile Number']#[0:10]
        pyemail = request.POST['Email']#[0:30]
        pyclgname = request.POST['College_Name']#[0:40]
        pybranch = request.POST['Branch']#[0:20]
        pyreport = request.POST['Report']#[0:10]
        pyprofile = request.POST['Profile']

        if A_1_Salasar.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/a_1_Salasar.html')
        if A_1_Salasar.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/a_1_Salasar.html')

        data2 = A_1_Salasar(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, reporting_time = pyreport, profile=pyprofile, confirmation=1)
        data2.save()
        messages.success(request, "Successfully registered.")
        with open('A_1_Salasar.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([pyname, pymob, pyemail, pyclgname, pybranch, pyreport, pyprofile])

        # email(pyemail)
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


def ibm(request):
    if request.method == 'GET':
        return render(request, 'tpo/ibm.html')

    if request.method == 'POST' and 'register' in request.POST:
        pyfname = request.POST['Student_Name']
        pysname = request.POST['Student_Name2']
        pymob = request.POST['Mobile Number']#[0:10]
        pyemail = request.POST['Email']#[0:30]
        pyclgname = request.POST['College_Name']#[0:40]
        pybranch = request.POST['Branch']
        # pyslot = request.POST['Slot']#[0:20]

        if zycus.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/ibm.html')
        if zycus.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/ibm.html')

        data2 = zycus(firstname=pyfname, lastname=pysname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, confirmation=1)
        data2.save()
        messages.success(request, "Successfully registered.")
        # with open('ibm.csv', 'a', newline='') as csvfile:
        #     filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     filewriter.writerow([pyname, pymob, pyemail, pyclgname, pybranch])
        # email(pyemail)
        return render(request, 'tpo/ibm.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        if zycus.objects.filter(number2=pymob2).exists():
            zycus.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed for {pymob2}")
            return render(request, 'tpo/ibm.html')
        else:
            messages.error(request, f"The number {pymob2} is not registered")
            return render(request, 'tpo/ibm.html')

