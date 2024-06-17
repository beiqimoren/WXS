from django.db import models
# 用户信息
# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    unit = models.CharField(max_length=128)     #单位名称
    province = models.CharField(max_length=32)  # 装备所在地省
    city = models.CharField(max_length=32)  # 市
    address = models.CharField(max_length=128)  #用户驻地位置
    boss = models.CharField(max_length=32)      #可选择用户的上级账户
class AdminUserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    unit = models.CharField(max_length=128)    #单位名称
    area = models.CharField(max_length=1000)   #辖区
# 装备报修单
class RepairTable(models.Model):
    userID = models.IntegerField()               #用户ID
    equipment= models.CharField(max_length=64)   #装备名称
    type = models.CharField(max_length=64)       #装备型号
    province = models.CharField(max_length=32)   #装备所在地省
    city = models.CharField(max_length=32)       #市
    address = models.CharField(max_length=64)    #详细地址
    fault = models.CharField(max_length=128)     #故障现象
    contact = models.CharField(max_length=32)    #联系人
    phone = models.CharField(max_length=32)      #联系电话
    unit = models.CharField(max_length=64)       #单位名称
    notes = models.CharField(max_length=64)      #备注
    state = models.CharField(max_length=32)      #状态或回执
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

class MyConsultMsg(models.Model):
    consultID = models.IntegerField()
    type = models.IntegerField()
    content = models.CharField(max_length=256)

