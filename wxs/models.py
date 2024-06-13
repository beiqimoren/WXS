from django.db import models
# 用户信息
# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    unit = models.CharField(max_length=128)     #单位名称
    address = models.CharField(max_length=128)  #用户驻地位置
    boss = models.CharField(max_length=32)      #可选择用户的上级账户
class AdminUserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    unit = models.CharField(max_length=128)    #单位名称
    area = models.CharField(max_length=1000)   #辖区
# 装备报修单
class RepairTable(models.Model):
    userID = models.IntegerField()
    equipment= models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    fault = models.CharField(max_length=128)
    contact = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    unit = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
# 技术支援申请单
class SupportTable(models.Model):
    userID = models.IntegerField()
    date= models.CharField(max_length=64)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    thing = models.CharField(max_length=128)
    contact = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    unit = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
# 消息
class MyMsg(models.Model):
    adminID = models.IntegerField()
    userID = models.IntegerField()
    date = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    state = models.CharField(max_length=32)

class MyConsult(models.Model):
    adminID = models.IntegerField()
    userID = models.IntegerField()
    title = models.CharField(max_length=256)
    contentlist = models.CharField(max_length=9999)
