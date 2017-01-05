#!/usr/bin/python
# -*- coding: utf8 -*-
import os,socket
import zlib,urllib,time
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
    startserver()
startserver()#随脚本一同启动服务
ERRTIMES=3#允许出错次数
proxies={
    'http':'http://127.0.0.1:8000',#手动设置http代理
    'https':'https://127.0.0.1:8000'#手动设置https代理
    #'http':os.getenv("http_proxy")#从系统获取http代理（Linux支持）
}
socket.setdefaulttimeout(5)#连接超时
i,v,vv=0,0,0
while 1:
    try:
        t=urllib.urlopen(
            'http://www.google.com/intl/',
             proxies=proxies,
        )
        v=zlib.crc32(t.read())
        if v!=vv and vv:
            #页面数据不一致处理
            i+=1
            print "error",v,vv,i
            if i>ERRTIMES:
                #重启服务
                restartserver()
                i=0
        else:
            #页面数据一致处理
            print "well",i
        vv=v
    except Exception,e:
        #超时或无法连接处理
        i+=1
        print e,i
        if i>ERRTIMES:
            #重启服务
            restartserver()
            i=0
    time.sleep(10)#检测间隔时间
