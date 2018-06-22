# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from jc import models
from jc import dao
from jc import sql
from jc import util
from jc.elk import elkservice
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

bu=sql.business()#创建业务的实例
ma=sql.master()#创建主机实例
ne=sql.net()#创建网络实例
op=sql.operation()#自动化运维
intu=sql.ind()#创建首页的实例
port=sql.report()#创建报表实例
#业务监控数据封装
def jk(request):
    list=[]
    tuple=bu.jk()
    tump=0
    x=0
    y=0
    for i in tuple:
        tump=i[2]
        x+=1
        if x>len(tuple)-1:
            continue
        if  tump==tuple[x][2]:
            continue
        di={}
        for j in tuple:
            if tump==j[2]:
                y += 1
                dic={}
                dic['fathername']=j[0]
                dic['sonname']=j[1]
                dic['fatherid']=j[2]
                dic['sonid']=j[3]
                dic['nodeid']=j[4]
                dic['healthy']=j[5]
                # print dic
                di[y]=dic
        list.append(di)
    tr=util.format1(list)
    # print(list)
    return HttpResponse(tr)

#主机异常情况数据组装
def warninglog(request):
    warn=ma.wa()
    li=[]
    i=0
    for w in warn:
        i+=1
        wt = {}
        if i==1:
            wt['total']=w[0]
        else:
            wt['ip'] = w[0]
            wt['motorroom'] = w[1]
            wt['service'] = w[2]
            wt['error'] = w[3]
            wt['date'] = w[4]
        li.append(wt)
    wa=util.format1(li)
    return HttpResponse(wa)
#主机详情
def details(request):
    id=int(request.GET.get('id',0))
    cabinteid=int(request.GET.get('cabinteid',0))
    if id!=0:
        de=ma.eq1(id)
        dt=util.format1(de)
        return HttpResponse(dt)
    else:
        if cabinteid!=0:
            ad=ma.eq2(cabinteid)
            ab=util.format1(ad)
            return HttpResponse(ab)

        else:
            return HttpResponse('未曾查询到数据')
#网络端口详情
def portdescript(request):
    id=5
    if request.GET.get('id',0) !=0:
         id=int(request.GET['id'])
    ps=ne.qr(id)
    pt=util.format1(ps)
    return HttpResponse(json.dumps(ps,ensure_ascii=False))
#当前异常
def nowerror(request):
    num=request.GET.get('num',0)
    type=request.GET.get('type',0)
    ou=op.nowerror(int(num),int(type))
    li = []
    i = 0
    for w in ou:
        i += 1
        wt = {}
        if i == 1:
            wt['total'] = w[0]
        else:
            wt['ip'] = w[0]
            wt['error'] = w[1]
            wt['urgency'] = w[2]
            wt['service']=w[3]
            wt['date']=w[4].strftime("%Y-%m-%d %H:%S:%M")
        li.append(wt)
    return HttpResponse(json.dumps(li,ensure_ascii=False))
#主机管理
def mainop(request):
    num = request.GET.get('num', 0)
    mp=util.format1(op.mainop(num))
    return HttpResponse(mp)

def querymp(request):
    ip=request.GET.get('ip','null')
    os=request.GET.get('os','null')
    qp=op.querymp(str(ip),str(os))
    return HttpResponse(util.format1(qp))

#首页代码封装
def index(request):
    statu=request.GET.get('ind',0)
    it=intu.iny(int(statu))
    li = []
    i = 0
    for w in it:
        i += 1
        wt = {}
        if i == 1:
            wt['total'] = w[0]
            wt['test']='紧急待处理'
        elif i==2:
            wt['total']=w[0]
            wt['test'] = '待处理总数'
        elif i==3:
            wt['total'] = w[0]
            wt['test'] = '异常总数'
        else:
            wt['date'] = w[0].strftime("%Y-%m-%d %H:%S:%M")
            wt['ip'] = w[1]
            wt['service'] = w[2]
            wt['error'] = w[3]
            wt['errgency'] = w[4]
        li.append(wt)
    return HttpResponse(json.dumps(li,ensure_ascii=False))


#网络报表数据
def netport(request):
    farthid=request.GET.get('fartherid',1)
    sonid=request.GET.get('sonid',0)
    branchid=request.GET.get('branchid',0)
    if sonid==0:
        li = []
        w={}
        num1=0
        num2=0
        num3=0
        num4=0
        fathider = port.netfatherlist()
        fa={}
        for k in fathider:
            num1 += 1
            wt={}
            wt['fatherid']=k[0]
            wt['name']=k[1]
            fa[num1]=wt
        w['networkType']=fa
        sonider = port.netsonlist(int(farthid))
        for i in sonider[0:1]:
            sonid=i[0]
        son={}
        for j in sonider:
            num2+=1
            wt={}
            wt['sonid']=j[0]
            wt['sonname']=j[1]
            son[num2]=wt
        w['filiale']=son
        if sonid!=0:
            branch = port.branchlist(int(sonid))
            if branch:
                bh = {}
                for j in branch:
                    wt = {}
                    num4 += 1
                    wt['branchid'] = j[0]
                    wt['branname'] = j[1]
                    bh[num4] = wt
                w['area'] = bh
                for i in branch[0:1]:
                    branchid = i[0]
                netdata = port.netbranchdata(int(branchid))
                ne = {}
                for x in netdata:
                    num3 += 1
                    wt = {}
                    wt['id'] = x[0]
                    if x[1]:
                        stro = str(x[1]).split(',')
                        if len(stro) == 2:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = None
                        elif len(stro) == 3:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = stro[2]
                    else:
                        wt['networkType'] = None
                        wt['filiale'] = None
                        wt['area'] = None
                    wt['name'] = x[2]
                    wt['type'] = x[3]
                    wt['portnum'] = x[4]
                    ne[num3] = wt
                w['data'] = ne
            else:
                netdata = port.netportdata(sonid)
                ne = {}
                for x in netdata:
                    num3 += 1
                    wt = {}
                    wt['id'] = x[0]
                    if x[1]:
                        stro = str(x[1]).split(',')
                        if len(stro) == 2:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = None
                        elif len(stro) == 3:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = stro[2]
                    else:
                        wt['networkType'] = None
                        wt['filiale'] = None
                        wt['area'] = None
                    wt['name'] = x[2]
                    wt['type'] = x[3]
                    wt['portnum'] = x[4]
                    ne[num3] = wt
                w['data'] = ne
        li.append(w)
        return HttpResponse(json.dumps(li, ensure_ascii=False))
    else:
        branch = port.branchlist(int(sonid))
        la = []
        w = {}
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        fathider = port.netfatherlist()
        fa = {}
        for k in fathider:
            num1 += 1
            wt = {}
            wt['fatherid'] = k[0]
            wt['name'] = k[1]
            fa[num1] = wt
        w['networkType'] = fa
        sonider = port.netsonlist(int(farthid))
        son = {}
        for j in sonider:
            num2 += 1
            wt = {}
            wt['sonid'] = j[0]
            wt['sonname'] = j[1]
            son[num2] = wt
        w['filiale'] = son
        if branch:
            bh = {}
            for j in branch:
                wt = {}
                num4 += 1
                wt['branchid'] = j[0]
                wt['branname'] = j[1]
                bh[num4] = wt
            w['area'] = wt
            if branchid==0:
                netdata = port.netportdata(sonid)
                ne = {}
                for x in netdata:
                    num3 += 1
                    wt = {}
                    wt['id'] = x[0]
                    if x[1]:
                        stro = str(x[1]).split(',')
                        if len(stro) == 2:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = None
                        elif len(stro) == 3:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = stro[2]
                    else:
                        wt['networkType'] = None
                        wt['filiale'] = None
                        wt['area'] = None
                    wt['name'] = x[2]
                    wt['type'] = x[3]
                    wt['portnum'] = x[4]
                    ne[num3] = wt
                w['data'] = ne
            else:
                netdata = port.netbranchdata(int(branchid))
                ne = {}
                for x in netdata:
                    num3 += 1
                    wt = {}
                    wt['id'] = x[0]
                    if x[1]:
                        stro = str(x[1]).split(',')
                        if len(stro) == 2:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = None
                        elif len(stro) == 3:
                            wt['networkType'] = stro[0]
                            wt['filiale'] = stro[1]
                            wt['area'] = stro[2]
                    else:
                        wt['networkType'] = None
                        wt['filiale'] = None
                        wt['area'] = None
                    wt['name'] = x[2]
                    wt['type'] = x[3]
                    wt['portnum'] = x[4]
                    ne[num3] = wt
                w['data'] = ne
        else:
            netdata = port.netportdata(sonid)
            ne = {}
            for x in netdata:
                num3 += 1
                wt = {}
                wt['id'] = x[0]
                if x[1]:
                    stro = str(x[1]).split(',')
                    if len(stro) == 2:
                        wt['networkType'] = stro[0]
                        wt['filiale'] = stro[1]
                        wt['area'] = None
                    elif len(stro) == 3:
                        wt['networkType'] = stro[0]
                        wt['filiale'] = stro[1]
                        wt['area'] = stro[2]
                else:
                    wt['networkType'] = None
                    wt['filiale'] = None
                    wt['area'] = None
                wt['name'] = x[2]
                wt['type'] = x[3]
                wt['portnum'] = x[4]
                ne[num3] = wt
            w['data'] = ne
        la.append(w)
        return HttpResponse(json.dumps(la,ensure_ascii=False))

#查询网络报表
def quarynetreport(request):
    ip=request.GET.get('ip','null')
    type=request.GET.get('type','null')
    name=request.GET.get('name','null')
    if ip=='null'and type=='null'and name=='null':
        return HttpResponse('查询方式有误')
    else:
        qp=port.quarynetreport(str(ip),str(type),str(name))
        li=[]
        for i in qp:
            wt={}
            wt['id']=i[0]
            try:
                if i[1]:
                    stro = str(i[1]).split(',')
                    if len(stro) == 2:
                        wt['networkType']=stro[0]
                        wt['filiale']=stro[1]
                        wt['area'] = None
                    elif len(stro)==3:
                        wt['networkType'] = stro[0]
                        wt['filiale'] = stro[1]
                        wt['area'] = stro[2]
                else:
                    wt['networkType'] =None
                    wt['filiale'] =None
                    wt['area'] = None
            except Exception as e:
                print(e.message)
            wt['name']=i[2]
            wt['type']=i[3]
            wt['portnum']=i[4]
            li.append(wt)
        return HttpResponse(json.dumps(li,ensure_ascii=False))

#网络表报详情
def netreport(request):
    id=request.GET.get('id',0)
    nd=port.netportdetails(int(id))
    li=[]
    if nd:
        for i in nd:
            wt = {}
            wt['portindex'] = i[0]
            wt['port'] = i[1]
            wt['ip'] = i[2]
            li.append(wt)
    else:
        li.append('没有数据')
    return HttpResponse(json.dumps(li,ensure_ascii=False))
#(ip,port,timerange="00:00~23:59",interval="1h",type="hour"):
def netreportdata(request):
    ip=request.GET.get('ip',"null")
    port=request.GET.get('portindex',0)
    starttime=request.GET.get('starttime','null')
    stoptime=request.GET.get('stoptime','null')
    interval=request.GET.get('interval','null')
    if interval=='null':
        return HttpResponse('有误')
    else:
        data=elkservice.netdatareport(str(ip),str(port),str(starttime),str(stoptime),str(interval))
        return HttpResponse(json.dumps(data,ensure_ascii=False))
#ping报表数据封装
def pingreport(request):
    type=request.GET.get('type','day')
    page=request.GET.get('page',1)
    pt=port.pingreport()
    li=[]
    vi = []
    t={}
    for i in pt:
        data=elkservice.pingreport(i[0],type)
        stro = str(i[1]).split(',')
        for j in data:
            wt={}
            wt['date']=j['time']
            wt['ip']=i[0]
            wt['filiale'] = stro[1]
            wt['avgdelay']=j['avgdelay']
            wt['maxdelay']=j['maxdelay']
            wt['lostpercent']=j['lostpercent']
            li.append(wt)
    t['total']=len(li)
    vi=li[ (int(page)-1)*10:10*(int(page))]
    vi.append(t)
    return HttpResponse(json.dumps(vi,ensure_ascii=False))














