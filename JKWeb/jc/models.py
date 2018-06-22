# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jc import util
# Create your models here.
#机房的表结构
class motorroom(models.Model):
    id=models.AutoField(primary_key=True)#机房编号
    name=models.CharField(max_length=80,null=True)#机房名称
    layoutmap=models.CharField(max_length=80,null=True)#机房布局图

    def __unicode__(self):
        return str(self.id)
    class Meta:
        db_table='motorroom'

#机柜的表结构
class cabinet(models.Model):
    id=models.AutoField(primary_key=True)#机柜编号
    motorroomid=models.ForeignKey(motorroom)#机房编号
    name=models.CharField(max_length=80)#机柜名称


    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'cabinet'

# 分组表结构
class grouper(models.Model):
    id = models.AutoField(primary_key=True)#分组编号
    name = models.CharField(max_length=50,null=True)#名称
    fathergroup = models.IntegerField(null=True)#父分组
    branchgrouper=models.IntegerField(null=True)#子分组


    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table='grouper'

#设备的表结构
class equipment (models.Model):
    id=models.AutoField(primary_key=True)#设备编号
    name=models.CharField(max_length=80,null=True)#设备名称
    cabinetid=models.ForeignKey(cabinet)#机柜编号
    type=models.CharField(max_length=50,null=True)#设备类型
    brand=models.CharField(max_length=50,null=True)#设备品牌
    model=models.CharField(max_length=50,null=True)#设备型号
    username=models.CharField(max_length=50,null=True)#用户名
    password=models.CharField(max_length=50,null=True)#密码
    superpassword=models.CharField(max_length=50,null=True)#超级密码
    address=models.CharField(max_length=80,null=True)#地点
    role=models.CharField(max_length=50,null=True)#角色
    loginmode=models.CharField(max_length=50,null=True)#登陆方式
    edition=models.CharField(max_length=50,null=True)#版本
    groupid=models.ForeignKey(grouper,null=True)#分组编号
    wbstopdate=models.DateTimeField(null=True)#维保截至日期
    personliable=models.CharField(max_length=50,null=True)#责任人
    liablephone=models.CharField(max_length=50,null=True)#责任人联系电话
    buytime=models.DateTimeField(null=True)#购买时间
    serialnumber=models.CharField(max_length=80,null=True)#序列号
    tradename=models.CharField(max_length=50,null=True)#厂家名称
    startusetime=models.DateTimeField(null=True)#开始使用时间
    purpose=models.CharField(max_length=50,null=True)#用途
    wbcs=models.CharField(max_length=50,null=True)#维保厂商
    wbstart=models.DateTimeField(null=True)#维保开始时间
    ip=models.CharField(max_length=100,null=True)#ip地址
    os=models.CharField(max_length=50,null=True)#操作系统
    bitsize=models.CharField(max_length=50,null=True)#操作系统位数
    hostname=models.CharField(max_length=50,null=True)#主机名
    totalmemory=models.CharField(max_length=50,null=True)#总内存
    totaldisk=models.CharField(max_length=50,null=True)#总硬盘大小
    net_groupid_id=models.IntegerField(null=True)
    community=models.CharField(max_length=50,null=True)
    agentstatu=models.CharField(max_length=50,null=True)#agent状态
    ping=models.CharField(max_length=50,null=True)#是否加入ping

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table='equipment'


#主机监控表结构
class hostmonitoring(models.Model):
    id=models.AutoField(primary_key=True)#监控编号
    equipmentid=models.ForeignKey(equipment,null=True)#设备编号
    cpuavailability=models.CharField(max_length=50,null=True)#CPU利用率
    ramavailability=models.CharField(max_length=50,null=True)#内存利用率
    cardstatu=models.CharField(max_length=50,null=True)#板卡状态
    monitoringtime=models.DateTimeField(null=True)#监控时间点
    equipmentstatu=models.CharField(max_length=50,null=True)#设备状态
    diskspaceavailability=util.JsonField()#磁盘空间利用率
    netdelay=models.CharField(max_length=50,null=True)#网络延迟
    netcardtraffic=util.JsonField()#网卡流量
    diskio=util.JsonField()#磁盘

    class Meta:
        db_table='hostmonitoring'


#网络设备监控表结构
class networkdevicemonitor(models.Model):
    id=models.AutoField(primary_key=True)#监控编号
    equipmentid=models.ForeignKey(equipment)#设备编号
    portid=models.IntegerField(null=True)#端口编号
    portstatu=models.CharField(max_length=20,null=True)#端口状态
    linkbandwidth=models.CharField(max_length=50,null=True)#链路带宽
    avgdelay=models.FloatField(max_length=20,null=True)#平均延迟
    packetloss=models.CharField(max_length=20,null=True)#丢包率
    portavguse=models.CharField(max_length=20,null=True)#端口平均使用率
    portpeakvalueuse=models.CharField(max_length=20,null=True)#端口峰值使用率
    netdelay=models.FloatField(max_length=20,null=True)#网络延迟
    rateout=models.CharField(max_length=50,null=True)#速率出
    ratein=models.CharField(max_length=50,null=True)#速率入
    portdescribe=models.CharField(max_length=200,null=True)#端口描述

    class Meta:
        db_table='networkdevicemonitor'


#大业务表结构
class bigbusiness(models.Model):
    id=models.AutoField(primary_key=True)#业务编号
    name=models.CharField(max_length=80,null=True)#业务名称
    type=models.CharField(max_length=50,null=True)#业务类型
    linkman=models.CharField(max_length=50,null=True)#联系人
    phone=models.CharField(max_length=50,null=True)#联系电话
    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'bigbusiness'


#小业务表结构
class smallbusiness(models.Model):
    id = models.AutoField(primary_key=True)#业务编号
    name = models.CharField(max_length=80, null=True)#业务名称
    type = models.CharField(max_length=50, null=True)#业务类型
    linkman = models.CharField(max_length=50, null=True)#联系人
    phone = models.CharField(max_length=50, null=True)#联系电话
    fatherbusiness=models.ForeignKey(bigbusiness)#父业务
    whetherbusiness=models.CharField(max_length=50,null=True)#是否是自身业务
    branch = models.IntegerField(null=True)  # 子业务

    class Meta:
        db_table='smallbusiness'

 #业务主机关系表结构
class businessression(models.Model):
    id=models.AutoField(primary_key=True)#业务关系编号
    businessid=models.IntegerField(null=True)#业务编号
    equipmentid=models.ForeignKey(equipment)#主机编号
    type=models.CharField(max_length=20,null=True)#业务类型

    class Meta:
        db_table='businessression'

#业务设备链路表结构
class bueqlink(models.Model):
    id=models.AutoField(primary_key=True)
    businessid=models.IntegerField(null=True)#业务编号
    type=models.CharField(max_length=50,null=True)#业务类型
    mainstartid=models.IntegerField(null=True)#主机开始点编号
    mainstopid=models.IntegerField(null=True)#主机结束点编号
    ordernumer=models.IntegerField(null=True)#序号
    currenteqid=models.IntegerField(null=True)#当前设备点编号
    portid=models.IntegerField(null=True)#端口编号
    upeqid=models.IntegerField(null=True)#下个设备点编号

    class Meta:
        db_table='bueqlink'

class task(models.Model):
    id=models.AutoField(primary_key=True)#任务编号
    name=models.CharField(max_length=80,null=True)#任务名称
    target=models.CharField(max_length=50,null=True)#目标
    whetherdispatch=models.CharField(max_length=50,null=True)#是否已调度

    def __unicode__(self):
        return str(self.id)
    class Meta:
        db_table='task'

#调度白表结构
class schedule(models.Model):
    id=models.AutoField(primary_key=True)#编号
    name=models.CharField(max_length=50,null=True)#调度名称
    timeregexp=models.CharField(max_length=80,null=True)#调度时间表达式
    taskidlist=models.IntegerField(null=True)#任务编号列表
    statu=models.CharField(max_length=50,null=True)#状态

    def __unicode__(self):
        return  str(self.id)
    class Meta:
        db_table='schedule'


#任务执行结果表
class taskexecute(models.Model):
    id=models.AutoField(primary_key=True)#编号
    taskid=models.ForeignKey(task,null=True)#任务编号
    excuteresult=models.CharField(max_length=50,null=True)#执行结果
    excutetime=models.DateTimeField(null=True)#执行时间
    usetime=models.FloatField(max_length=20,null=True)#用时
    scheduleid=models.ForeignKey(schedule)#调度编号

    class Meta:
        db_table='taskexecute'

#网络报表表结构
class netreportforms(models.Model):
    id=models.AutoField(primary_key=True)#编号
    avgportflow=models.CharField(max_length=20,null=True)#平均端口流量
    peakvalueportflow=models.CharField(max_length=20,null=True)#峰值端口流量
    avgportuse=models.FloatField(max_length=20,null=True)#平均端口利用率
    peakvalueportuse=models.FloatField(max_length=20,null=True)#峰值端口利用率
    reportfromscycle=models.CharField(max_length=50,null=True)#报表周期
    reportfromtime=models.DateTimeField(null=True)#报表日期

    class Meta:
        db_table='netreportforms'

#警告日志表结构
class warninglog(models.Model):
    id=models.AutoField(primary_key=True)#编号
    linkman=models.CharField(max_length=80,null=True)#联系人
    phone=models.CharField(max_length=50,null=True)#电话
    correlationeq=models.IntegerField(null=True)#关联设备
    correlationport=models.IntegerField(null=True)#关联端口
    correlationbus=models.IntegerField(null=True)#关联任务
    faultdescription=models.CharField(max_length=200,null=True)#故障描述
    urgency=models.CharField(max_length=100,null=True)#紧急程度
    date=models.DateTimeField(null=True)#日期
    type=models.IntegerField(null=True)#类型


    class Meta:
        db_table='warninglog'

#警告阈值表结构
class warningthreshold(models.Model):
    id=models.AutoField(primary_key=True)#编号
    type=models.CharField(max_length=50,null=True)#警告类型
    groupid=models.ForeignKey(grouper)#分组编号
    target=models.CharField(max_length=50,null=True)#指标
    number=models.CharField(max_length=50,null=True)#数字

    class Meta:
        db_table='warningthreshold'

#网络设备端口表
class netequipmentport(models.Model):
    id=models.AutoField(primary_key=True)#编号
    portindex=models.IntegerField(null=True)
    port=models.CharField(max_length=50,null=True)
    potdescribe=models.CharField(max_length=100,null=True)
    portfullname=models.CharField(max_length=100,null=True)
    ip=models.CharField(max_length=50,null=True)
    ifInOctets=models.BigIntegerField(null=True)
    ifOutOctets=models.BigIntegerField(null=True)
    ifInErrors=models.BigIntegerField(null=True)
    ifOutErrors=models.BigIntegerField(null=True)
    ifSpeed=models.BigIntegerField(null=True)
    equipmentid=models.IntegerField(null=True)
    datatime=models.DateTimeField(null=True)
    inuseage=models.FloatField(null=True)
    outuseage=models.FloatField(null=True)
    inspeed=models.FloatField(null=True)
    outspeed=models.FloatField(null=True)
    usetime=models.FloatField(null=True)

    class Meta:
        db_table="netequipmentport"


















