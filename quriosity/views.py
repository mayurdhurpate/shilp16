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

def winners(request):
    slot = request.GET.get('slot', '')
    key = request.GET.get('key', '')
    if key=="i-dont-give-a-shit":
        if slot=='1':
            teams = [['49', 1], ['694', 2], ['285', 2], ['191', 2], ['658', 2], ['226', 2], ['488', 2], ['678', 3], ['656', 3], ['381', 3], ['437', 3], ['331', 3], ['497', 4], ['654', 4], ['617', 4], ['714', 5], ['305', 5], ['507', 5], ['653', 5], ['190', 6], ['157', 6], ['7', 7], ['716', 7], ['262', 7], ['297', 7], ['582', 7], ['506', 7], ['348', 7], ['371', 8], ['242', 8], ['433', 8], ['74', 8], ['689', 8], ['526', 9], ['706', 9], ['119', 9], ['440', 9], ['258', 9], ['732', 9], ['674', 9], ['680', 9], ['696', 10], ['695', 10], ['284', 10], ['625', 10], ['632', 10], ['316', 10], ['679', 10], ['407', 11], ['115', 11], ['366', 11], ['336', 11], ['185', 11], ['551', 11], ['208', 11], ['650', 12], ['189', 12], ['210', 13], ['676', 13], ['423', 13], ['740', 13], ['479', 13], ['660', 14], ['690', 14], ['698', 14], ['541', 14], ['418', 14], ['703', 14], ['584', 14], ['249', 14], ['557', 14], ['283', 15], ['274', 15], ['521', 15], ['244', 15], ['311', 15], ['635', 15], ['220', 15], ['729', 15], ['238', 15], ['140', 15], ['614', 15], ['134', 16], ['545', 16], ['712', 16], ['533', 16], ['243', 16], ['337', 16], ['253', 16], ['504', 16], ['636', 16], ['225', 16], ['559', 16], ['5', 16], ['671', 16], ['487', 16], ['687', 16], ['263', 17], ['265', 17], ['269', 17], ['294', 17], ['364', 17], ['646', 17], ['575', 17], ['67', 17], ['700', 17], ['353', 17], ['618', 17], ['287', 18], ['707', 18], ['81', 18], ['368', 18], ['177', 18], ['508', 18], ['633', 18], ['465', 18], ['314', 18], ['742', 18], ['744', 18], ['615', 18], ['717', 19], ['419', 19], ['199', 19], ['313', 19], ['420', 19], ['645', 19], ['651', 19], ['192', 19], ['553', 19], ['55', 20], ['538', 20], ['524', 20], ['3', 20], ['382', 20], ['156', 20], ['187', 20], ['99', 20], ['168', 20], ['158', 20], ['235', 20], ['464', 20], ['686', 20], ['59', 21], ['53', 21], ['361', 21], ['543', 22], ['268', 22], ['51', 22], ['318', 22], ['705', 22], ['114', 22], ['627', 22], ['66', 22], ['106', 22], ['182', 22], ['503', 22], ['14', 22], ['552', 22], ['480', 22], ['684', 22], ['340', 23], ['12', 23], ['728', 23], ['600', 23], ['692', 24], ['4', 24], ['90', 24], ['709', 24], ['587', 24], ['576', 24], ['344', 24], ['602', 24], ['211', 25], ['499', 25], ['367', 25], ['390', 25], ['101', 25], ['435', 25], ['221', 25], ['236', 25], ['681', 25], ['701', 26], ['483', 26], ['673', 27], ['411', 27], ['591', 27], ['317', 27], ['702', 27], ['383', 27], ['386', 27], ['642', 27], ['630', 27], ['603', 27], ['328', 27], ['380', 28], ['402', 28], ['685', 28], ['229', 29]]
        if slot=='2':
            teams = [['77', 0], ['362', 0], ['347', 0], ['666', 0], ['770', 0], ['856', 0], ['883', 0], ['149', 1], ['152', 1], ['141', 1], ['336', 1], ['409', 1], ['462', 1], ['536', 1], ['260', 1], ['766', 1], ['834', 1], ['832', 1], ['879', 1], ['857', 1], ['874', 1], ['85', 2], ['343', 2], ['384', 2], ['308', 2], ['649', 2], ['547', 2], ['672', 2], ['746', 2], ['738', 2], ['736', 2], ['789', 2], ['293', 2], ['123', 3], ['188', 3], ['151', 3], ['230', 3], ['357', 3], ['528', 3], ['612', 3], ['599', 3], ['840', 3], ['792', 3], ['796', 3], ['764', 3], ['617', 3], ['786', 3], ['837', 3], ['882', 3], ['887', 3], ['388', 3], ['884', 3], ['75', 4], ['222', 4], ['241', 4], ['365', 4], ['393', 4], ['345', 4], ['477', 4], ['416', 4], ['489', 4], ['550', 4], ['641', 4], ['731', 4], ['776', 4], ['808', 4], ['852', 4], ['703', 4], ['65', 5], ['333', 5], ['439', 5], ['441', 5], ['415', 5], ['493', 5], ['129', 5], ['667', 5], ['713', 5], ['788', 5], ['822', 5], ['784', 5], ['791', 5], ['774', 5], ['865', 5], ['864', 5], ['848', 5], ['606', 5], ['859', 5], ['869', 5], ['542', 5], ['850', 5], ['58', 6], ['116', 6], ['146', 6], ['273', 6], ['278', 6], ['271', 6], ['212', 6], ['307', 6], ['355', 6], ['639', 6], ['350', 6], ['725', 6], ['683', 6], ['818', 6], ['428', 6], ['823', 6], ['824', 6], ['790', 6], ['816', 6], ['861', 6], ['804', 6], ['475', 6], ['846', 6], ['860', 6], ['360', 6], ['89', 7], ['96', 7], ['175', 7], ['319', 7], ['356', 7], ['432', 7], ['454', 7], ['414', 7], ['624', 7], ['727', 7], ['733', 7], ['721', 7], ['838', 7], ['835', 7], ['870', 7], ['424', 7], ['827', 7], ['601', 7], ['862', 7], ['110', 7], ['54', 7], ['878', 7], ['71', 8], ['103', 8], ['64', 8], ['10', 8], ['204', 8], ['252', 8], ['226', 8], ['302', 8], ['251', 8], ['259', 8], ['295', 8], ['323', 8], ['281', 8], ['342', 8], ['320', 8], ['394', 8], ['436', 8], ['467', 8], ['459', 8], ['548', 8], ['531', 8], ['621', 8], ['699', 8], ['841', 8], ['797', 8], ['828', 8], ['817', 8], ['767', 8], ['814', 8], ['62', 9], ['69', 9], ['184', 9], ['202', 9], ['267', 9], ['286', 9], ['359', 9], ['427', 9], ['406', 9], ['628', 9], ['652', 9], ['803', 9], ['773', 9], ['873', 9], ['339', 9], ['710', 9], ['708', 9], ['60', 10], ['57', 10], ['142', 10], ['128', 10], ['280', 10], ['395', 10], ['445', 10], ['802', 10], ['868', 10], ['100', 10], ['598', 10], ['616', 10], ['431', 10], ['877', 10], ['300', 11], ['250', 11], ['240', 11], ['245', 11], ['329', 11], ['595', 11], ['655', 11], ['754', 11], ['798', 11], ['810', 11], ['762', 11], ['885', 11], ['891', 11], ['88', 12], ['87', 12], ['254', 12], ['449', 12], ['748', 12], ['739', 12], ['775', 12], ['831', 12], ['855', 12], ['95', 12], ['867', 12], ['242', 12], ['255', 13], ['219', 13], ['466', 13], ['400', 13], ['607', 13], ['594', 13], ['592', 13], ['765', 13], ['836', 13], ['854', 13], ['844', 13], ['872', 13], ['853', 13], ['107', 14], ['451', 14], ['580', 14], ['568', 14], ['556', 14], ['517', 14], ['839', 14], ['819', 14], ['799', 14], ['842', 14], ['644', 14], ['135', 14], ['888', 14], ['875', 14], ['124', 15], ['257', 15], ['326', 15], ['574', 15], ['752', 15], ['800', 15], ['863', 15], ['787', 15], ['234', 16], ['398', 16], ['239', 16], ['94', 17], ['148', 17], ['228', 17], ['246', 17], ['438', 17], ['520', 17], ['503', 17], ['585', 17], ['881', 17], ['147', 18], ['399', 18], ['751', 18], ['215', 18], ['843', 18], ['131', 19], ['501', 19], ['165', 20], ['270', 20], ['845', 20], ['352', 21], ['191', 29]]
        winners = []
        for team in teams:
            t = Team.objects.get(id=int(team[0]))
            winners.append(t)
        return render(request, 'winners.html', {'winners': winners})
