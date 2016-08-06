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

def conclave(request):
    return render(request,"city.html",{},RequestContext(request))

def register(request):
    return render(request,"register.html",{},RequestContext(request))

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

def pptsubmit(request):
    if request.method=='POST':
        u=PPTUser.objects.create(title=request.POST['title'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    designation = request.POST['designation']   ,
                                    college=request.POST['college'],
                                    author=request.POST['author'] ,
                                    coauthor=request.POST['coauthor'])
        return HttpResponse('Your response have been recorded.')
    return HttpResponse('Authentication failed.')