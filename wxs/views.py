from django.shortcuts import render,HttpResponse
from wxs import models
# Create your views here.
def index(request):
    return render(request,"index.html")
    return HttpResponse('这是首页！')

# 用户登录验证
def login(request):
    username = request.GET['username']
    if models.UserInfo.objects.filter(username=username).first().password == request.GET['password']:
        return HttpResponse("成功")
    return HttpResponse('失败')

# 注册用户
def sigup(request):
    username = request.GET['username']
    password = request.GET['password']
    models.UserInfo.objects.create(username=username, password=password)
    ff = models.UserInfo.objects.all().values('username', 'password')
    return HttpResponse(ff)
