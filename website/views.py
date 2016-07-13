from django.shortcuts import render
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
