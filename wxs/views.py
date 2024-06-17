import json

from django.contrib.postgres import serializers
from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wxs import models
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.
def index(request):
    return render(request, "index.html")
    return HttpResponse('这是首页！')


def login(request):
    username = request.GET['param']
    password = request.GET['param1']
    if (models.UserInfo.objects.filter(username=username).exists()):
        obj = models.UserInfo.objects.filter(username=username).first()
        if (obj.password == password):
            return JsonResponse({
                'state': "成功",
                'userID': obj.id
            })
        return JsonResponse({
            'state': "密码错误",
            'userID': 0
        })
    return JsonResponse({
        'state': "用户不存在",
        'userID': 0
    })


# 注册用户
@require_http_methods(["POST"])
@csrf_exempt
def sigup(request):
    try:
        data = json.loads(request.body)
        if models.UserInfo.objects.filter(username=data.get("username")).exists():
            return JsonResponse({
                'state': "该账号已注册",
                'userID': 0
            })
        if models.UserInfo.objects.create(username=data.get("username"),
                                       password=data.get("password"),
                                       province=data.get("province"),
                                       city=data.get("city"),
                                       unit=data.get("unit"),
                                       address=data.get("city"),
                                       boss=''
                                          ):
            return JsonResponse({
                'state': "注册成功",
                'username': 0
            })
        return JsonResponse({
            'state': "注册失败",
            'username': 0
        })
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


@require_http_methods(["POST"])
@csrf_exempt
def addrepairtable(request):
    try:
        data = json.loads(request.body)
        if models.RepairTable.objects.create(userID=data.get("userID"),
                                             equipment=data.get("equipment"),
                                             type=data.get("type"),
                                             province=data.get("province"),
                                             city=data.get("city"),
                                             address=data.get("address"),
                                             fault=data.get("fault"),
                                             contact=data.get("contact"),
                                             phone=data.get("phone"),
                                             unit=data.get("unit"),
                                             notes=data.get("notes"),
                                             state=data.get("state")):
            return HttpResponse("成功")
        return HttpResponse("失败")
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


@require_http_methods(["POST"])
@csrf_exempt
def addsupporttable(request):
    try:
        data = json.loads(request.body)
        if models.SupportTable.objects.create(userID=data.get("userID"),
                                              date=data.get("date"),
                                              province=data.get("province"),
                                              city=data.get("city"),
                                              address=data.get("address"),
                                              thing=data.get("thing"),
                                              contact=data.get("contact"),
                                              phone=data.get("phone"),
                                              unit=data.get("unit"),
                                              notes=data.get("notes"),
                                              state=data.get("state")):
            return HttpResponse("成功")
        return HttpResponse("失败")
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


def select_repair_byuserID(request):
    userID = int(request.GET['param'])
    data = {}
    if models.RepairTable.objects.filter(userID=userID).exists():
        data['repairTable'] = list((models.RepairTable.objects.filter(userID=userID)).values())
        return JsonResponse(data)
    data['repairTable'] = "没有数据"
    return JsonResponse(data)


def select_repair_byid(request):
    id = int(request.GET['id'])
    if models.RepairTable.objects.filter(id=id).exists():
        result = model_to_dict(models.RepairTable.objects.get(id=id))
        return HttpResponse(json.dumps(result), content_type="application/json")


def select_support_byuserID(request):
    userID = int(request.GET['param'])
    data = {}
    if models.SupportTable.objects.filter(userID=userID).exists():
        data['supportTable'] = list((models.SupportTable.objects.filter(userID=userID)).values())
        return JsonResponse(data)
    data['supportTable'] = "没有数据"
    return JsonResponse(data)


def getmsg(request):
    userID = int(request.GET['param'])
    data = {}
    if models.MyMsg.objects.filter(userID=userID).exists():
        data['mymsg'] = list((models.MyMsg.objects.filter(userID=userID)).values())
        return JsonResponse(data)
    data['mymsg'] = "没有数据"
    return JsonResponse(data)

@require_http_methods(["POST"])
@csrf_exempt
def addconsult(request):
    try:
        data = json.loads(request.body)
        myconsult = models.MyConsult(userID=data.get("userID"), adminID=data.get("adminID"), title=data.get("title"), contentlist=data.get("content"))
        myconsult.save()
        myconsultmsg = models.MyConsultMsg(consultID=myconsult.id, type=0, content=data.get("content"))
        myconsultmsg.save()
        return HttpResponse("成功")
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


def getconsult(request):
    userID = int(request.GET['param'])
    data = {}
    if models.MyConsult.objects.filter(userID=userID).exists():
        data['myconsult'] = list((models.MyConsult.objects.filter(userID=userID)).values())
        return JsonResponse(data)
    data['myconsult'] = "没有数据"
    return JsonResponse(data)

def getconsultbyID(request):
    consultID = int(request.GET['param'])
    data = {}
    if models.MyConsultMsg.objects.filter(consultID=consultID).exists():
        data['myconsultbyID'] = list(models.MyConsultMsg.objects.filter(consultID=consultID).order_by('id').values())
        return JsonResponse(data)
    data['myconsultbyID'] = "没有数据"
    return JsonResponse(data)

@require_http_methods(["POST"])
@csrf_exempt
def updateconsult(request):
    try:
        data = json.loads(request.body)
        if models.MyConsultMsg.objects.create(consultID=data.get("consultID"), type=data.get("type"), content=data.get("content")):
            return HttpResponse("成功")
        return HttpResponse("失败")
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
@require_http_methods(["POST"])
@csrf_exempt
def admin_login(request):
    data=(json.loads(request.body))
    username = data.get('account')
    password = data.get('password')
    if (models.AdminUserInfo.objects.filter(username=username).exists()):
        obj = models.AdminUserInfo.objects.filter(username=username).first()
        if (obj.password == password):
            return HttpResponse({obj.id}, status=200)
        return HttpResponse({"密码错误！"}, status=201)
    return HttpResponse({"用户不存在！"}, status=202)


def admin_getrepair(request):
    state = request.GET["state"]
    page = request.GET["page"]
    adminID = request.GET["adminID"]
    areas = models.AdminUserInfo.objects.filter(id=adminID).values('area')
    arealist=((areas[0])['area']).split(',')
    userids = models.UserInfo.objects.filter(city__in=arealist).values('id')
    useridlist = []
    for userid in userids:
        useridlist.append(userid['id'])
    if state=='':
        datalist = models.RepairTable.objects.filter(userID__in=useridlist)
    else:
        datalist = models.RepairTable.objects.filter(userID__in=useridlist,state=state)
    paginator = Paginator(datalist, 10)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    data = {'result': []}
    for item in results.object_list:
        data['result'].append({
            'id': item.id,
            'userID' : item.userID,
            'equipment': item.equipment,
            'type' : item.type,
            'province' : item.province,
            'city' : item.city,
            'address' : item.address,
            'fault': item.fault,
            'contact' : item.contact,
            'phone' : item.phone,
            'unit': item.unit,
            'notes' : item.notes,
            'state' : item.state
        })
    data['total'] = paginator.count
    return JsonResponse(data, status=200)

def admin_viewrepair(request):
    ID = request.GET["id"]
    data = {}
    data['result'] = list(models.RepairTable.objects.filter(id=ID).values())
    return JsonResponse(data, status=200)


def admin_changerepairstate(request):
    ID = request.GET["id"]
    state = request.GET["state"]
    if models.RepairTable.objects.filter(id=ID).update(state=state):
        return HttpResponse("修改成功！",status=200)
    return HttpResponse("修改失败！", status=400)


def admin_getsupport(request):
    state = request.GET["state"]
    page = request.GET["page"]
    adminID = request.GET["adminID"]
    areas = models.AdminUserInfo.objects.filter(id=adminID).values('area')
    arealist = ((areas[0])['area']).split(',')
    userids = models.UserInfo.objects.filter(city__in=arealist).values('id')
    useridlist = []
    for userid in userids:
        useridlist.append(userid['id'])
    if state == '':
        datalist = models.SupportTable.objects.filter(userID__in=useridlist)
    else:
        datalist = models.SupportTable.objects.filter(userID__in=useridlist, state=state)
    paginator = Paginator(datalist, 10)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    data = {'result': []}
    for item in results.object_list:
        data['result'].append({
            'id': item.id,
            'userID': item.userID,
            'date': item.date,
            'province': item.province,
            'city': item.city,
            'address': item.address,
            'thing': item.thing,
            'contact': item.contact,
            'phone': item.phone,
            'unit': item.unit,
            'notes': item.notes,
            'state': item.state
        })
    data['total'] = paginator.count
    return JsonResponse(data, status=200)


def admin_viewsupport(request):
    ID = request.GET["id"]
    data = {}
    data['result'] = list(models.SupportTable.objects.filter(id=ID).values())
    return JsonResponse(data, status=200)


def admin_changesupportstate(request):
    ID = request.GET["id"]
    state = request.GET["state"]
    if models.SupportTable.objects.filter(id=ID).update(state=state):
        return HttpResponse("修改成功！", status=200)
    return HttpResponse("修改失败！", status=400)