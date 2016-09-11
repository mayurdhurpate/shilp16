from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
import hashlib
from datetime import datetime
from django.utils import timezone
from .models import *

questions = {}
slots = {}

def home(request):
    if is_authenticated(request):
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

        if name and pwd:
            if not Team.objects.filter(name=name).exists():
                t = Team(name=name, password=pwd, slot=slot)
            else:
                return JsonResponse({'msg': 'Team name already exists!!', 'error': True})
        else:
            return JsonResponse({'msg': 'Enter valid Team name and Password', 'error': True})

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

        request.session['name'] = name
        request.session['secret'] = name+'random_stuff'+pwd
        return JsonResponse({'error': False, 'msg': 'logging you in.'})
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

        if name and pwd:
            try:
                t = Team.objects.get(name=name)
            except Exception:
                return JsonResponse({'error': True, 'msg': 'Team dosn\'t exists.'})
            if t.password == pwd:
                request.session['secret'] = name+'random_stuff'+pwd
                request.session['name'] = name
                return JsonResponse({'error': False, 'msg': 'logging you in.'})
            else:
                return JsonResponse({'error': True, 'msg': 'Password is incorrect.'})
        else:
            return JsonResponse({'msg': 'Enter valid credentials'})
    else:
        return redirect('/quriosity')

def dashboard(request):
    t = is_authenticated(request)
    if t:
        context = {}
        slot = t.slot
        if slots.has_key(t.slot):
            s = slots[t.slot]
        else:
            slots[t.slot] = Slot.objects.get(title=slot)
            s = slots[t.slot]
        now = timezone.now()
        if s.start <= now and s.end >= now:
            context['diff'] = (s.end - now).total_seconds()
            if questions.has_key(t.slot):
                context['questions'] = questions.get(t.slot)
            else:
                questions[t.slot] = s.question.all().order_by('score')
                context['questions'] = questions[t.slot]
            context['team'] = t
            return render(request, "dashboard.html", context)
        else:
            context['diff'] = (s.start - now).total_seconds()
            context['team'] = t
            return render(request, "waiting.html", context)
    else:
        return redirect('/quriosity')

def details(request):
    t = is_authenticated(request)
    if t:
        if request.method == "POST":
            members = t.members.all()
            for i in xrange(len(members)):
                members[i].phone=request.POST['phone'+str(i+1)].strip()
                members[i].college=request.POST['clg'+str(i+1)].strip()
                members[i].year=request.POST['year'+str(i+1)].strip()
                members[i].gender=request.POST['sex'+str(i+1)].strip()
                try:
                    members[i].save()
                except Exception as e:
                    return JsonResponse({'erorr': True, 'msg': e})
            return redirect('dashboard')
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
            num = request.POST.get('num', '')
            if slots.has_key(t.slot):
                s = slots[t.slot]
            else:
                slots[t.slot] = Slot.objects.get(title=slot)
                s = slots[t.slot]
            now = timezone.now()
            if response and num and s.start <= now and s.end >= now:
                try:
                    if int(num) == 1:
                        t.response1 = response
                        t.save()
                    elif int(num) == 2:
                        t.response2 = response
                        t.save()
                    elif int(num) == 3:
                        t.response3 = response
                        t.save()
                    elif int(num) == 4:
                        t.response4 = response
                        t.save()
                    elif int(num) == 5:
                        t.response5 = response
                        t.save()
                    elif int(num) == 6:
                        t.response6 = response
                        t.save()
                    elif int(num) == 7:
                        t.response7 = response
                        t.save()
                    elif int(num) == 8:
                        t.response8 = response
                        t.save()
                    elif int(num) == 9:
                        t.response9 = response
                        t.save()
                    elif int(num) == 10:
                        t.response10 = response
                        t.save()
                    elif int(num) == 11:
                        t.response11 = response
                        t.save()
                    elif int(num) == 12:
                        t.response12 = response
                        t.save()
                    elif int(num) == 13:
                        t.response13 = response
                        t.save()
                    elif int(num) == 14:
                        t.response14 = response
                        t.save()
                    elif int(num) == 15:
                        t.response15 = response
                        t.save()
                    else:
                        return JsonResponse({'error': True, 'msg': 'Some Error occured'})
                except Exception as e:
                    return JsonResponse({'error': True, 'msg': 'Error in saving response. Contact support.'})
                return JsonResponse({'error': False, 'msg': 'Your answer is recorded!'})
            else:
                return JsonResponse({'error': True, 'msg': 'Enter valid response!'})
        else:
            return JsonResponse({'error': True, 'msg': 'Do a POST request.'})
    else:
        return JsonResponse({'error': True, 'msg': 'Unauthenticated request!'})

def logout(request):
    if is_authenticated(request):
        del request.session['name']
        del request.session['secret']
    return redirect('/quriosity')

def is_authenticated(request):
    name = request.session.get('name', '')
    if name:
        try:
            t = Team.objects.get(name=name)
            if t.name+'random_stuff'+t.password == request.session.get('secret',''):
                return t
        except:
            pass

def allu(request):
    key = request.GET.get('key', '')
    if key=="i-dont-give-a-shit":
        users = QUser.objects.all()
        return render(request, "users.html", {'users': users})
    else:
        return HttpResponse('Unauthenticated access')


def res(request):
    key = request.GET.get('key', '')
    if key=="i-dont-give-a-shit":
        responses = Response.objects.all()
        return render(request, 'responses.html', {'responses': responses})
    else:
        return HttpResponse('Unauthenticated access')
