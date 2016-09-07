from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
import hashlib
from datetime import datetime
from django.utils import timezone
from .models import *

def home(request):
    t = is_authenticated(request)
    if t:
        return redirect('dashboard')
    else:
        return render(request, 'home.html', {})

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        slot = request.POST.get('slot', 1)
        memnum = request.POST.get('mem', 1)
        name1 = request.POST.get('name1', '')
        email1 = request.POST.get('email1', '')
        phone1 = request.POST.get('phone1', '')

        if name and not Team.objects.filter(name=name).exists():
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

        if int(memnum) == 2:
            u2.save()
            t.members.add(u2)

        # send_mail("Quriosity'16: Embrace curiosity",
        #     "Thanks for registering for Quriosity'16.\nFor any quries contact quriosity@shilpiitbhu.org",
        #     'no-reply@shilpiitbhu.org',
        #     r, fail_silently=False)

        return JsonResponse({'error': False, 'msg': 'Thanks for registering. For your information check your mail after sometime.'})
    else:
        return redirect('/quriosity')

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

def login(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')

        if name != '' and pwd != '':
            t = Team.objects.get(name=name)
            if t and t.password == pwd:
                res = JsonResponse({'error': False, 'msg': 'logging you in.'})
                res.set_cookie('GA001', hashlib.sha224(name+'random_stuff'+pwd).hexdigest())
                res.set_cookie('name', name)
                return res
            elif t:
                return JsonResponse({'error': True, 'msg': 'Password is incorrect.'})
            else:
                return JsonResponse({'error': True, 'msg': "Team name doesn\'t exists"})
        else:
            return JsonResponse({'msg': 'Enter valid credentials'})
    else:
        return redirect('/quriosity')

def dashboard(request):
    t = is_authenticated(request)
    if t:
        context = {}
        if Slot.objects.get(title=t.slot).start <= timezone.now() and Slot.objects.get(title=t.slot).end >= timezone.now():
            context['diff'] = (Slot.objects.get(title=t.slot).end - timezone.now()).total_seconds()
            context['questions'] = Slot.objects.get(title=t.slot).question.all().order_by('score')
            context['team'] = t 
            return render(request, "dashboard.html", context)
        else:
            context['diff'] = (Slot.objects.get(title=t.slot).start - timezone.now()).total_seconds()
            context['team'] = t
            return render(request, "waiting.html", context)
    else:
        return redirect('home')

def details(request):
    t = is_authenticated(request)
    if t:
        if request.method == "POST":
            members = t.members.all()
            phone1 = request.POST.get('phone-1', '')
            clg1 = request.POST.get('clg-1', '')
            year1 = request.POST.get('year-1','')
            gender1 = request.POST.get('sex-1','')
            members[0].phone = phone1
            members[0].college = clg1
            members[0].year = year1
            members[0].gender = gender1
            members[0].save()
            if len(members) == 2:
                phone2 = request.POST.get('phone-2', '')
                clg2 = request.POST.get('clg-2', '')
                year2 = request.POST.get('year-2','')
                gender2 = request.POST.get('sex-2','')
                members[1].phone = phone2
                members[1].college = clg2
                members[1].year = year2
                members[1].gender = gender2
                members[1].save()                
            return redirect('/quriosity/dashboard')
        else:
            members = t.members.all()
            return render(request, "details.html", {'members': members, 'num': len(members)})
    else:
        return redirect('/quriosity')

def question(request, qid):
    t = is_authenticated(request)
    if t:
        if request.method == "POST":
            response = request.POST.get('ans', '')
            s = Slot.objects.get(title=t.slot)
            if response and s.start <= timezone.now() and s.end >= timezone.now():
                r, created = Response.objects.get_or_create(question_id=qid, team=t)
                r.response = response
                r.save()
                return JsonResponse({'error': False, 'msg': 'Your answer is recorded!'})
            else:
                return JsonResponse({'error': True, 'msg': 'Enter valid response!'})
        else:
            return JsonResponse({'error': True, 'msg': 'Do a POST request.'})
    else:
        return JsonResponse({'error': True, 'msg': 'Unauthenticated request!'})

def logout(request):
    t = is_authenticated(request)
    if t:
        res = redirect('/quriosity')
        res.set_cookie('GA001', '')
        return res
    else:
        return redirect('/quriosity')

def is_authenticated(request):
    c = request.COOKIES.get('GA001', '')
    try:
        t = Team.objects.get(name=request.COOKIES.get('name', ''))
        if hashlib.sha224(t.name+'random_stuff'+t.password).hexdigest() == c:
            return t
    except:
        pass
