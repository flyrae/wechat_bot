# -*- coding: utf-8 -*-
import urllib,urllib2
import sys
import json
import itchat,time,re
from itchat.content import *

reload(sys) 
sys.setdefaultencoding('utf-8') 
API_KEY = '059e1bb85d61463380b05a0086f37c98'
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

def result(get_msg):
    for i in range(1,100):
        queryStr = get_msg
        TULINURL = "%s%s" % (raw_TULINURL,urllib2.quote(queryStr))
        req = urllib2.Request(url=TULINURL)
        result = urllib2.urlopen(req).read()
        hjson=json.loads(result)
        length=len(hjson.keys())
        content=hjson['text']

        if length==3:
            return content+hjson['url']
        elif length==2:
            return content

@itchat.msg_register([TEXT])
def text_reply(msg):
    # match = re.search('年',msg['TEXT']).span()
    # if match:
    print 'hj'
    print msg['Text'].encode('utf-8')
    contents = result(msg['Text'].encode('utf-8'))
    print contents
    itchat.send(contents.decode('utf-8'),msg['FromUserName'])
@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def other_reply(msg):
    itchat.send(('鸡年大吉'),msg['FromUserName'])
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run()

            