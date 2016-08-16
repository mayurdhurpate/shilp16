from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = "home.html"

def signup(request):
    name = request.POST.get('name', '')
    pwd = request.POST.get('pwd', '')
    slot = request.POST.get('slot', '')
    name1 = request.POST.get('name1', '')
    email1 = request.POST.get('email1', '')
    phone1 = request.POST.get('phone1', '')
    name2 = request.POST.get('name2', '')
    email2 = request.POST.get('email2', '')
    phone2 = request.POST.get('phone2', '')
    return HttpResponse('hi')