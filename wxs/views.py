import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from wxs import models


# Create your views here.
def index(request):
    return render(request, "index.html")
    return HttpResponse('这是首页！')


# 用户登录验证
# def login(request):
#     username = request.GET['username']
#     passored = request.GET['password']
#     obj=models.UserInfo.objects.filter(username=username).first()
#     response = HttpResponse("Hello, World!")
#     response.status_code =222
#     if obj.password == passored:
#         response = HttpResponse(obj.id)
#         response.status_code = 111
#     return response


def login(request):
    username = request.GET['username']
    password = request.GET['password']
    if(models.UserInfo.objects.filter(username=username).exists()):
        obj = models.UserInfo.objects.filter(username=username).first()
        if(obj.password == password):
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
    username = request.GET['username']
    password = request.GET['password']
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
        return JsonResponse({'status': 'success', 'data': data})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
