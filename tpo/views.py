from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method == 'GET':
        return render(request, 'tpo/home.html')
    if request.POST:
        pyname = request.POST['Student_Name']
        pymob = request.POST['Mobile Number']
        pyemail = request.POST['Email']
        pyclgname = request.POST['College Name']
        pybranch = request.POST['Branch']
        pyslot = request.POST['Slot']
        #confmob = request.POST['username']
        # count = User.objects.count()
        # count += 1
        data = Student(name=pyname, number2=pymob, email=pyemail, clg_name=pyclgname, branch=pybranch, slot=pyslot)
        data.save()
        email(request)
        return render(request, 'tpo/home.html')


def about(request):
    return render(request, 'tpo/about.html')


def authenticate(request):
    form = UserCreationForm()
    return render(request, 'tpo/authenticate.html', {'form': form})
    
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['anujssmishra@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
#    return redirect('redirect to a new page')
