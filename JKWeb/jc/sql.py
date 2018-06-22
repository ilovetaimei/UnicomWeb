# -*- coding: utf-8 -*-
from django.db import connection


#业务监控类
class business:
    def jk(self):
        cursor = connection.cursor()
        #查询业务关联
        cursor.execute( 'select a.name1,a.name,a.id2,a.id,a.branch,w.id from (select  b.name as name1,s.name,s.id,b.id as id2,s.branch from bigbusiness b left join smallbusiness s on b.id=s.fatherbusiness_id ) as a left join warninglog w on a.id=w.correlationbus ')
        tuple = cursor.fetchall()
        cursor.close()
        return tuple
#主机状态
class master:
    #查询当前异常主机
    def wa(self):
        cursor = connection.cursor()
        cur=connection.cursor()
        cur.execute('select count(*) from warninglog w,smallbusiness s,equipment e,cabinet c,motorroom m where w.correlationbus=s.id and w.correlationeq=e.id and e.cabinetid_id=c.id and c.motorroomid_id=m.id')
        cursor.execute( 'select  e.ip,m.name,s.type,w.faultdescription,w.date from warninglog w,smallbusiness s,equipment e,cabinet c,motorroom m where w.correlationbus=s.id and w.correlationeq=e.id and e.cabinetid_id=c.id and c.motorroomid_id=m.id')
        warn = cursor.fetchall()
        wq=cur.fetchall()
        we=wq+warn
        cursor.close()
        cur.close()
        return we
    def eq1(self,id):
        cursor = connection.cursor()
        cursor.execute('select * from equipment where id=%s', id)
        de = cursor.fetchall()
        cursor.close()
        return de

    def eq2(self,id):
        cursor = connection.cursor()
        cursor.execute('select * from equipment e,cabinet c where e.cabinetid_id=c.id and c.id=%s', id)
        ad = cursor.fetchall()
        cursor.close()
        return ad
    def kpI(self):
        cursor = connection.cursor()

#网络状况
class net:

    def qr(self,id):
        cursor = connection.cursor()
        cursor.execute(
            'select n.portid,s.name,n.portstatu,n.ratein,n.rateout,n.packetloss,n.portdescribe from networkdevicemonitor n,bueqlink b,bigbusiness s where n.portid=b.portid and b.businessid=s.id and n.equipmentid_id=%s',
            id)
        ps = cursor.fetchall()
        cursor.close()
        return ps

    def nteqma(self,num):
        cursor = connection.cursor()
        cursor.execute('select e.ip,e.hostname,e.type,e.agentstatu,e.ping from equipment e ,grouper g  order by e.id limit {0},5'.format(5*num))

#自动化运维
class operation:
    def nowerror(self,num,type):
        cursor = connection.cursor()
        cur = connection.cursor()
        cur.execute('select count(*) from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id ')
        if num!=0:
            cursor.execute('select  e.ip,w.faultdescription,w.urgency,s.type,w.date from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id order by w.id limit {0},5'.format(5*num))
        else:
            cursor.execute( 'select  e.ip,w.faultdescription,w.urgency,s.type,w.date from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id order by w.id limit 0,5')
        no=cur.fetchall()
        ne=cursor.fetchall()
        nt=no+ne
        cur.close()
        cursor.close()
        return nt
#基本信息
    def mainop(self,num):
        cursor = connection.cursor()
        cur = connection.cursor()
        cur.execute('select count(*) from equipment e ,businessression b ,bigbusiness s where e.id=b.equipmentid_id and b.businessid=s.id')
        if num!=0:
            cursor.execute( 'select e.ip,e.hostname,s.type,e.name,e.os,e.agentstatu,e.ping from equipment e ,businessression b ,bigbusiness s where e.id=b.equipmentid_id and b.businessid=s.id order by e.id limit {0},5'.format(5 * num))
        else:
            cursor.execute( 'select e.ip,e.hostname,s.type,e.name,e.os,e.agentstatu,e.ping from equipment e ,businessression b ,bigbusiness s where e.id=b.equipmentid_id and b.businessid=s.id order by e.id limit 0,5')

        mp=cur.fetchall()+cursor.fetchall()
        cursor.close()
        cur.close()
        return mp
#模糊查询
    def querymp(self,ip,os):
        cursor = connection.cursor()
        qp=None
        if ip!='null':
            cursor.execute(
                'select e.ip,e.hostname,s.type,e.name,e.os,e.agentstatu,e.ping from equipment e ,businessression b ,bigbusiness s where e.id=b.equipmentid_id and b.businessid=s.id and e.ip like %s order by e.id limit 0,5',ip)
            qp=cursor.fetchall()
        elif os !='null':
            cursor.execute(
                'select e.ip,e.hostname,s.type,e.name,e.os,e.agentstatu,e.ping from equipment e ,businessression b ,bigbusiness s where e.id=b.equipmentid_id and b.businessid=s.id and e.os like %s order by e.id limit 0,5',os)
            qp=cursor.fetchall()
        else:
            qp='有误'
        return qp

    def equimentdetairs(self):
        cursor = connection.cursor()
        cursor.execute('select e.hostname,e.os,e.totalmemory,g.type,e.totaldisk,e.ip from equipment e,businessression b ,bigbusiness g where b.equipmentid_id=e.id and b.businessid=g.id and e.id=5')
        ep=cursor.fetchall()
        cursor.close()
        return ep

    def Assetdetails(self):
        cursor = connection.cursor()
        cursor.execute('select e.personliable,e.liablephone,e.buytime,e.serialnumber,e.tradename,c.name,e.startusetime,e.purpose,e.wbcs,e.wbstart,e.wbstopdate from equipment e,cabinet c where e.cabinetid_id=c.id and e.id=5')
        ad=cursor.fetchall()
        cursor.close()
        return ad
    #设备详情
    def sbxq(self):
        cursor = connection.cursor()
        cursor.execute('')

    def ZDXJ(self,de,num):
        zg=None
        cursor = connection.cursor()
        cur=connection.cursor()
        if num!=0 and de=='null':
            cur.execute('select count(*) from equipment e , grouper g where g.id=e.groupid_id')
            cursor.execute('select e.hostname,e.type,e.agentstatu,g.name from equipment e , grouper g where g.id=e.groupid_id order by e.id limit {0},5'.format(num))
            zg=cur.fetchall()+cursor.fetchall()
        elif num!=0 and de!='null':
            cur.execute('select count(*) from equipment e , grouper g where g.id=e.groupid_id and e.ip like %s or e.hostname like %s',de)
            cursor.execute( 'select e.hostname,e.type,e.agentstatu,g.name from equipment e , grouper g where g.id=e.groupid_id and e.ip like %s or e.hostname like %s order by e.id limit {0},5'.format(num),de)
            zg = cur.fetchall() + cursor.fetchall()
        elif num==0 and de!='null':
            cur.execute('select count(*) from equipment e , grouper g where g.id=e.groupid_id and e.ip like %s or e.hostname like %s',de)
            cursor.execute('select e.hostname,e.type,e.agentstatu,g.name from equipment e , grouper g where g.id=e.groupid_id and e.ip like %s or e.hostname like %s order by e.id limit 0,5',de)
            zg = cur.fetchall() + cursor.fetchall()
        else:
            cur.execute('select count(*) from equipment e , grouper g where g.id=e.groupid_id')
            cursor.execute( 'select e.hostname,e.type,e.agentstatu,g.name from equipment e , grouper g where g.id=e.groupid_id order by e.id limit 0,5')
            zg = cur.fetchall() + cursor.fetchall()
        cur.close()
        cursor.close()
        return zg

class ind:

    def iny(self,statu):
        cursor = connection.cursor()
        cur = connection.cursor()
        cu= connection.cursor()
        ct= connection.cursor()
        sr=None
        try:
            cur.execute('select count(*) from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id and w.urgency=%s','严重')
            cu.execute('select count(*) from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id ')
            ct.execute('select count(*) from warninglog')
            if statu==0:
                cursor.execute(
                    'select w.date,e.ip,s.type,w.faultdescription,w.urgency from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id and w.urgency=%s order by w.id limit 0,5','严重')
            if statu==1:
                cursor.execute('select w.date,e.ip,s.type,w.faultdescription,w.urgency from warninglog w,equipment e ,smallbusiness s where  w.correlationeq=e.id and w.correlationbus=s.id order by w.id limit 0,5')
            st=cursor.fetchall()
            sy=cur.fetchall()
            su=cu.fetchall()
            si=ct.fetchall()
            sr=sy+su+si+st
        except Exception as e:
            print(e.message)
        cursor.close()
        cur.close()
        cu.close()
        ct.close()
        return sr

class  report:

    def netreport(self,fatherid,sonid):

        return None
    #获取父级目录
    def netfatherlist(self):
        cursor = connection.cursor()
        cursor.execute('select id,name from grouper where fathergroup=0  ')
        fathlist=cursor.fetchall()
        cursor.close()
        return fathlist
    #获取二级目录
    def netsonlist(self,fatherid):
        cursor = connection.cursor()
        cursor.execute('select id,name from grouper where fathergroup={0}'.format(fatherid))
        sonlist=cursor.fetchall()
        cursor.close()
        return sonlist

    #获取第三级目录
    def branchlist(self,sonid):
        cursor = connection.cursor()
        cursor.execute('select id,name from grouper where fathergroup={0} '.format(sonid))
        branch=cursor.fetchall()
        cursor.close()
        return branch
    #获取网络报表数据
    def netportdata(self,id):
        cursor = connection.cursor()
        cur = connection.cursor()
        cursor.execute('SELECT e.id,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname,e.hostname,e.type,(SELECT COUNT(*) AS count FROM netequipmentport t WHERE t.ip=e.ip) as con FROM equipment e  WHERE e.groupid_id={0} and e.ty!=%s '.format(id),'主机')
        cur.execute('SELECT e.id,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname,e.hostname,e.type,(SELECT COUNT(*) AS count FROM netequipmentport t WHERE t.ip=e.ip) as con FROM equipment e,(SELECT id  AS gid FROM grouper  WHERE fathergroup={0} ) AS p  WHERE e.groupid_id=p.gid and e.type !=%s'.format(id),'主机')
        nt=cursor.fetchall()
        nd=cur.fetchall()
        if nd:
            np = nt + nd
        else:
            np=nt
        cursor.close()
        cur.close()
        return np
    #获取三级报表信息

    def netbranchdata(self,branchid):
        cursor = connection.cursor()
        cursor.execute('SELECT e.id,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname,e.hostname,e.type,(SELECT COUNT(*) AS count FROM netequipmentport t WHERE t.ip=e.ip) as con FROM equipment e  WHERE e.groupid_id={0} and e.type !=%s'.format(branchid),'主机')
        bd=cursor.fetchall()
        cursor.close()
        return bd
#查询网络报表
    def quarynetreport(self,ip,type,name):
        cursor = connection.cursor()
        if ip!='null':
            cursor.execute('SELECT e.id,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname ,e.hostname,e.type,(SELECT COUNT(*) AS count FROM netequipmentport t WHERE t.ip=e.ip) as con from equipment e WHERE e.ip=%s',ip)
        elif type!='null':
            cursor.execute(
                'SELECT e.id,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname ,e.hostname,e.type,(SELECT COUNT(*) AS count FROM netequipmentport t WHERE t.ip=e.ip) as con from equipment e WHERE e.type=%s',
                type)
        elif name!='null':
            cursor.execute(
                'SELECT e.id,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname ,e.hostname,e.type,(SELECT COUNT(*) AS count FROM netequipmentport t WHERE t.ip=e.ip) as con from equipment e WHERE e.hostname=%s',
                name)
        qp=cursor.fetchall()
        cursor.close()
        return qp
#网络报表端口详情
    def netportdetails(self,id):
        cursor = connection.cursor()
        cursor.execute('SELECT n.portindex,n.`port`,n.ip from netequipmentport n,equipment e WHERE e.ip=n.ip AND e.id={0}'.format(id))
        nd=cursor.fetchall()
        cursor.close()
        return nd
#ping报表数据
    def pingreport(self):
        cursor = connection.cursor()
        cursor.execute('SELECT e.ip,(select group_concat(`name`)  from grouper g where FIND_IN_SET(g.id,getParLst(e.groupid_id))) as fname from equipment e WHERE e.ping=1')
        pt=cursor.fetchall()
        cursor.close()
        return pt













































