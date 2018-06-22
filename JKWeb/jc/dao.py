# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
from jc import models
from jc import util
from django.core import serializers
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
#查询机柜
def selectmotorroom(request):
    mo=serializers.serialize('json',models.motorroom.objects.all())
    me=util.format2(mo)
    return HttpResponse(me)
#查询分组
def selectgroup(request):
    gp=serializers.serialize('json',models.grouper.objects.all())
    gd=util.format2(gp)
    return HttpResponse(gd)
#是否加入ping
def addping(request):
    re=request.GET.get('ping','null')
    id=request.GET.get('id',0)
    if re=='yes'and id!=0:
        models.equipment.objects.filter(id=int(id)).update(ping=re)
        return HttpResponse('ok')
    elif re=='no'and id!=0:
        models.equipment.objects.filter(id=int(id)).update(ping=re)
        return HttpResponse('ok')
#网络设备管理
def neteqop(request):
    op=request.GET.get('type','null')
    num=request.GET.get('num',0)
    if num !=0 and op=='null':
        li = []
        gp=models.equipment.objects.values("ip","hostname","type","agentstatu").order_by("id")[num*5:num*5+5]
        for i in gp:
            li.append(i)
        return HttpResponse(util.format1(li))
    elif op!='null'and num!=0:
        li = []
        gt=models.equipment.objects.values("ip", "hostname", "type", "agentstatu").filter(Q(ip__icontains=op)|Q(hostname__icontains=op)).order_by("id")[num*5:num*5+5]
        for i in gt:
            li.append(i)
        return HttpResponse(util.format1(li))
    elif op!='null'and num==0:
        li = []
        gt=models.equipment.objects.values("ip", "hostname", "type", "agentstatu").filter(Q(ip__icontains=op)|Q(hostname__icontains=op)).order_by("id")[0:5]
        for i in gt:
            li.append(i)
        return HttpResponse(util.format1(li))
    else:
        li = []
        gp = models.equipment.objects.values("ip", "hostname", "type", "agentstatu").order_by("id")[0:5]
        for i in gp:
            li.append(i)
        return HttpResponse(util.format1(li))

def test(request):
    str='ok'
    #str=models.equipment.objects.values_list("businessression__id","hostname").filter(cabinetid__id=1)
    return HttpResponse(str)

















