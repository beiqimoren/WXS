"""
URL configuration for zbwx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from wxs import views

urlpatterns = [
    # 用户APP端接口
    path('index/', views.index),
    path('login/', views.login),
    path('sigup/', views.sigup),
    path('addrepairtable/', views.addrepairtable),
    path('addconsult/', views.addconsult),
    path('addsupporttable/', views.addsupporttable),
    path('select_repair_byuserID/', views.select_repair_byuserID),
    path('select_repair_byid/', views.select_repair_byid),
    path('select_support_byuserID/', views.select_support_byuserID),
    path('getmsg/', views.getmsg),
    path('getconsult/', views.getconsult),
    path('updateconsult/', views.updateconsult),
    path('getconsultbyID/', views.getconsultbyID),
    #后台管理端接口
    path('admin_login/', views.admin_login),
    path('admin_getrepair/', views.admin_getrepair),
    path('admin_viewrepair/', views.admin_viewrepair),





]
