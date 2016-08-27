from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

from .models import *

class HomeView(TemplateView):
    template_name = "home.html"

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        slot = request.POST.get('slot', 1)
        memnum = request.POST.get('mem', 1)
        name1 = request.POST.get('name1', '')
        email1 = request.POST.get('email1', '')
        phone1 = request.POST.get('phone1', '')

        if not Team.objects.filter(name=name).exists():
            t = Team(name=name, password=pwd, slot=slot)
        else:
            return JsonResponse({'msg': 'Team name already exists!!', 'error': True})

        if name1 and email1 and phone1:
            if not QUser.objects.filter(email=email1).exists():
                u1 = QUser(name=name1, email=email1, phone=phone1)
            else:
                return JsonResponse({'msg': 'User exists with email: ' + email1, 'error': True})
        else:
            return JsonResponse({'msg': 'Enter valid data', 'error': True})

        if int(memnum) == 2:
            name2 = request.POST.get('name2', '')
            email2 = request.POST.get('email2', '')
            phone2 = request.POST.get('phone2', '')
            if name2 and email2 and phone2:
                if not QUser.objects.filter(email=email2).exists():
                    u2 = QUser(name=name2, email=email2, phone=phone2)
                else:
                    return JsonResponse({'msg': 'User exists with email: ' + email2, 'error': True})
            else:
                return JsonResponse({'msg': 'Enter valid data', 'error': True})
        t.save()
        u1.save()
        t.members.add(u1)
        r = [email1]

        if int(memnum) == 2:
            u2.save()
            t.members.add(u2)
            r.append(email2)

        # send_mail("Quriosity'16: Embrace curiosity",
        #     "Thanks for registering for Quriosity'16.\nFor any quries contact quriosity@shilpiitbhu.org",
        #     'no-reply@shilpiitbhu.org',
        #     r, fail_silently=False)

        return JsonResponse({'error': False, 'msg': 'Thanks for registering. For your information check your mail after sometime.'})
    else:
        return HttpResponse('Nothing for you here!! <s>Do a POST</s>')

def helpQ(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        msg = request.POST.get('msg', '')
        if name and email and msg:
            h = HelpQuestion.objects.create(name=name, email=email, message=msg)
            return JsonResponse({'error': False})
        else:
            return JsonResponse({'error': True, 'msg': 'Enter valid data.'})
    else:
        return JsonResponse({'error': True})