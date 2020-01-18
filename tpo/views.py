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
from .models import virtusa
from .models import lti20nov
from .models import lti12result
from .models import infosys15nov
from .models import cap20nov
from .models import lti28nov
from .models import bit9nov
from .models import swab12dec
from .models import zycus11jan
from .models import cap8jan
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# from django.core.mail import EmailMessage
import csv
# import os




# if not os.path.isfile('./lti.csv'):
# 	with open('lti.csv', 'w', newline='') as csvfile:
# 		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		filewriter.writerow(['Student_Name', 'Mobile Number','Email','College_Name','Branch','Qualification','10th Passing Year','10th Percentage','12th Passing Year','12th Percentage','Diploma Passing Year','Diploma Percentage','Aggregate Graduation Pointer','Degree Paassing Year','Nationality','TPO Name','TPO Number','TPO Email'])



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

def quality(request):
    return render(request,'tpo/quality.html')

def Infosys(request):
    return render(request,'tpo/infosys.html')

def harm(request):
    return render(request,'tpo/harm.html')

def ltionlymap(request):
    return render(request,'tpo/ltionlymap.html')

def wiproonlymap(request):
    return render(request,'tpo/wiproonlymap.html')

def paytm(request):
    return render(request,'tpo/capgemini.html')

def swabhav(request):
    return render(request,'tpo/capgemini21.html')

def virtresult(request):
    return render(request,'tpo/virtresult.html')

def cgdiv(request):
    return render(request,'tpo/cgdiv.html')

def Infofinalresult(request):
    studentdb = finalinfosys.objects.all()
    return render(request,'tpo/infoclglist.html', {'studentdb':studentdb})

def Lti12result(request):
    studentdb = lti12result.objects.all()
    return render(request,'tpo/ltiresult.html', {'studentdb':studentdb})

def Infofinalnameresult(request):
    studentdb = finallistinfosys.objects.all()
    return render(request,'tpo/infofinalnamelist.html', {'studentdb':studentdb})

def zycusaptilist(request):
    return render(request,'tpo/info15novresult.html')

def cap19novdata(request):
    return render(request,'tpo/cap1030.html')

def cap20novresult(request):
    return render(request,'tpo/cap20novresult.html')

def cap25novresult(request):
    return render(request,'tpo/zycusvedant.html')

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

def cap20db(request):
	studentdb = cap20nov.objects.all()
	count = cap20nov.objects.all().count()
	count2 = cap20nov.objects.filter(confirmation='1').count()
	return render(request, 'tpo/cap20novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def swab1212db(request):
	studentdb = swab12dec.objects.all()
	count = swab12dec.objects.all().count()
	count2 = swab12dec.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def bit912db(request):
	studentdb = bit9nov.objects.all()
	count = bit9nov.objects.all().count()
	count2 = bit9nov.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def zycus11jandb(request):
	studentdb = zycus11jan.objects.all()
	count = zycus11jan.objects.all().count()
	count2 = zycus11jan.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def cap8jandb(request):
	studentdb = cap8jan.objects.all()
	count = cap8jan.objects.all().count()
	count2 = cap8jan.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def lti2811db(request):
	studentdb = lti28nov.objects.all()
	count = lti28nov.objects.all().count()
	count2 = lti28nov.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti28novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def info15novdb(request):
	studentdb = infosys15nov.objects.all()
	count = infosys15nov.objects.all().count()
	count2 = infosys15nov.objects.filter(confirmation='1').count()
	return render(request, 'tpo/info15novdb.html', {'studentdb':studentdb,'count':count,'count2':count2})

def lti20db(request):
	studentdb = lti20nov.objects.all()
	count = lti20nov.objects.all().count()
	count2 = lti20nov.objects.filter(confirmation='1').count()
	return render(request, 'tpo/lti20db.html', {'studentdb':studentdb,'count':count,'count2':count2})

def ibmdatabase(request):
	studentdb = IBM.objects.all()
	count = IBM.objects.all().count()
	count2 = IBM.objects.filter(confirmation='1').count()
	return render(request, 'tpo/ibmdatabase.html', {'studentdb':studentdb,'count':count,'count2':count2})

def virtusadatabase(request):
	studentdb = virtusa.objects.all()
	count = virtusa.objects.all().count()
	count2 = virtusa.objects.filter(confirmation='1').count()
	return render(request, 'tpo/virtusadb.html', {'studentdb':studentdb,'count':count,'count2':count2})

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
# 	elif request.method == 'POST' and 'ltiemail_db' in request.POST:
# 		msg = EmailMessage('database file', 'hello', settings.EMAIL_HOST_USER, ['vedantmh@gmail.com','amvichare@apsit.edu.in','tpo@apsit.edu.in'])
# 		msg.content_subtype = "html"
# 		msg.attach_file('lti.csv')
# 		msg.send()
# 		messages.success(request, "Emailed Database.")
	return render(request, 'tpo/admin_panel.html')



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
        # pysname = request.POST['Student_Name2']
        pymob = request.POST['Mobile Number']#[0:10]
        pyemail = request.POST['Email']#[0:30]
        pyclgname = request.POST['College_Name']#[0:40]
        pybranch = request.POST['Branch']
        pydeg = request.POST['Deg_type']
        # pyslot = request.POST['Slot']
        # pyref = request.POST['Referral']

        if zycus11jan.objects.filter(number2=pymob).exists():
            messages.error(request, f"{pymob} already registered, use another")
            return render(request, 'tpo/ibm.html')
        if zycus11jan.objects.filter(email=pyemail).exists():
            messages.error(request, f"{pyemail} already registered, use another")
            return render(request, 'tpo/ibm.html')

        data2 = zycus11jan(name=pyfname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, degtype=pydeg, confirmation=1)
        data2.save()
        messages.success(request, "Successfully registered.")
        return render(request, 'tpo/ibm.html')

    if request.method == 'POST' and 'confirm' in request.POST:
        pymob2 = request.POST['confmob']
        # pyemail = request.POST['confemail']
        if (zycus11jan.objects.filter(number2=pymob2).exists()) and pymob2!="":
            zycus11jan.objects.filter(number2=pymob2).update(confirmation=1)
            messages.success(request, f"Presence confirmed")
            return render(request, 'tpo/ibm.html')

        # elif (zycus11jan.objects.filter(email=pyemail).exists()) and pyemail!="":
        #     zycus11jan.objects.filter(email=pyemail).update(confirmation=1)
        #     messages.success(request, f"Presence confirmed")
        #     return render(request, 'tpo/ibm.html')
        else:
            messages.error(request, f"Not registered")
            return render(request, 'tpo/ibm.html')

def Tolearn(request):
    return render(request,'tpo/Tolearn.html')

def capgemini8jan(request):
    return render(request,'tpo/capgemini8jan.html')

def capgemini10jan(request):
    return render(request,'tpo/capgemini10jan.html')

# def ycus11jan(request):
#     return render(request,'tpo/zycus11jan.html')

def lti14jan(request):
    return render(request,'tpo/lti14jan.html')
