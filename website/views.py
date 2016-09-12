from django.core.mail import send_mail
from django.shortcuts import render
from .models import *

from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,"index.html",{},RequestContext(request))

def ca(request):
    return render(request,"ca.html",{},RequestContext(request))

def idp(request):
    return render(request,"industry.html",{},RequestContext(request))

def ppt(request):
    return render(request,"presentation.html",{},RequestContext(request))


def workshop1(request):
    return render(request,"workshop1.html",{},RequestContext(request)) 

def workshop2(request):
    return render(request,"workshop2.html",{},RequestContext(request))       


def conclave(request):
    return render(request,"city.html",{},RequestContext(request))

def register(request):
    return render(request,"register.html",{},RequestContext(request))

def Staff(request):
    return render(request,"Staff.html",{},RequestContext(request)) 

def casubmit(request):
    if request.method=='POST':
        u=CAUser.objects.create(name=request.POST['name'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    promotion = request.POST['promotion']   ,
                                    college=request.POST['college'],
                                    year=request.POST['radio'],
                                    resume=request.POST['resume'])
        return HttpResponse('Your response have been recorded.')
    return HttpResponse('Authentication failed.')

def worksubmit(request):
    if request.method=='POST':
        print(request.POST)
        u=WorkUser.objects.create(name=request.POST['author'],
                                    designation=request.POST['designation'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    college=request.POST['college'])
        return HttpResponse('Your response have been recorded.')
    return HttpResponse('Authentication failed.')    

def pptsubmit(request):
    if request.method=='POST':
        u=PPTUser.objects.create(title=request.POST['title'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    designation = request.POST['designation']   ,
                                    college=request.POST['college'],
                                    author=request.POST['author'] ,
                                    coauthor=request.POST['coauthor'])
        
        send_mail(
            'Subject here',
            'Thanks for submission. We have recorded your response.\nTitle of Paper'+u.title+'\nName of 1st Author'+u.author+'\nCollege/university'
            +u.college+'\ndesignation'+u.designation+'\nCo-Author'+u.coauthor+'\nPhone No.'+u.phone+'\nEmail'+u.email,
            'no-reply@shilpiitbhu.org',
            [u.email],
            fail_silently=False,
        )
        return HttpResponse('Your response have been recorded.')
    return HttpResponse('Authentication failed.')



def regsubmit(request):
    if request.method=='POST':
        u=User.objects.create(event=request.POST['event'],
                                    teamname=request.POST['teamname'],
                                    teamleader=request.POST['teamleader'],
                                    Email= request.POST['Email']   ,
                                    college= request.POST['college']   ,
                                    mob_no=request.POST['mob_no'],
                                    year=request.POST['year'] ,)
                                   
        if "email1" in request.POST:
            u.tmem1=request.POST['tmem1']
            u.email1=request.POST['email1']
            u.mob1=request.POST['mob1']
        if "email2" in request.POST:   
            u.tmem2=request.POST['tmem2']
            u.email2=request.POST['email2']
            u.mob2=request.POST['mob2']
        if "email3" in request.POST:   
            u.tmem3=request.POST['tmem3']
            u.email3=request.POST['email3']
            u.mob3=request.POST['mob3']
        if "email4" in request.POST:
            u.tmem4=request.POST['tmem4']
            u.email4=request.POST['email4']
            u.mob4=request.POST['mob4']
        if "email5" in request.POST:    
            u.tmem5=request.POST['tmem5']
            u.email5=request.POST['email5']
            u.mob5=request.POST['mob5']
        u.query=""
        u.save()
        return HttpResponse('Your response have been recorded.')
    return HttpResponse('Authentication failed.')

