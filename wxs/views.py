import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from wxs import models


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
def sigup(request):
    username = request.GET['param']
    password = request.GET['param1']
    if models.UserInfo.objects.filter(username=username).exists():
        return JsonResponse({
            'state': "该账号已注册",
            'userID': 0
        })
    models.UserInfo.objects.create(username=username, password=password)
    return JsonResponse({
        'state': "注册成功",
        'username': 0
    })

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
    data['repairTable'] ="没有数据"
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
