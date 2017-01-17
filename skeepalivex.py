#!/usr/bin/python
# -*- coding: utf8 -*-
import os,socket,threading
import zlib,urllib,time
from bottle import route,run,template

def killserver():
    #os.system('killserver.bat')#Windows
    #os.system('./killserver.x.sh')#OS X
    os.system('./killserver.sh')#Linux
def startserver():
    global vv
    vv=0#重置页面基准
    #os.system('startserver.bat')#Windows
    #os.system('./startserver.x.sh')#OS X
    os.system('./startserver.sh')#Linux
def restartserver():
    killserver()
    time.sleep(3)
    startserver()
startserver()#随脚本一同启动服务
ERRTIMES=5#允许出错次数
serverlist=[{
    "ip":"127.0.0.1",#http/https服务器地址
    "port":"8000",#http/https服务器端口
    "stat":0,#记录服务器状态
    "index":0#优先级，数值越小越优先，数值相同为平行优先级。
    #区别说明：当高优先级的服务器恢复后会自动切回高优先级的服务器，平行优先级的服务器顺序轮流使用。
},{
    "ip":"127.0.0.1",
    "port":"8100",
    "stat":0,
    "index":1
}]
socket.setdefaulttimeout(10)#连接超时
@route('/pac')
def pac():#获取负载均衡的pac文件
    return template("pac",serverip=ip,serverport=port)
@route('/info')
def info():#获取服务器状态
    serverstat={
        'ip':'',
        'port':''
    }
    info=template(u'服务器{{serverip}}:{{serverport}} 状态{{serverstat}}',
                  serverip=ip,
                  serverport=port,
                  serverstat=serverstat)
    return info
#启动http服务器，用于生产负载均衡的pac文件
#threading.Thread(target=run, args=(host='localhost', port=8080)).start()
threading.Thread(target=run, args=()).start()#上面语法有误，暂时用默认值
i,v,vv=0,0,0
ip,port="",""
while 1:
    for server in serverlist:
        try:
            ip,port=server["ip"],server["port"]
            proxies={
                'http':'http://%s:%s'%(ip,port),#手动设置http代理
                'https':'https://%s:%s'%(ip,port)#手动设置https代理
                #'http':os.getenv("http_proxy")#从系统获取http代理（Linux支持）
            }
            t=urllib.urlopen(
                'http://www.google.com/intl/',
                 proxies=proxies,
            )
            v=zlib.crc32(t.read())
            if v!=vv and vv:
                #页面数据不一致处理
                i+=1
                print "error","%s:%s"%(ip,port),v,vv,i
                if i>ERRTIMES:
                    #重启服务
                    restartserver()
                    i=0
            else:
                #页面数据一致处理
                print "well","%s:%s"%(ip,port),i
                i=0#清空计数器，这里不清空可以累计出错次数，清空为连续出错次数
                vv=v
                break
            vv=v
        except Exception,e:
            #超时或无法连接处理
            i+=1
            print "%s:%s"%(ip,port),e,i
            if i>ERRTIMES:
                #重启服务
                restartserver()
                i=0
    time.sleep(10)#检测间隔时间
