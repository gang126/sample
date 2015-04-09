#coding: utf-8
import requests
import re,time
import json
import urllib
import base64
import rsa
import binascii
#from weibo import APIClient

url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.5)&_=1364875106625'
session=requests.Session()

ret =session.get(url_prelogin)
#print ret.content
'''
l=re.findall('"servertime":(\d+),.*?"nonce":"(.*?)","pubkey":"(.*?)","rsakv":"(.*?)"',ret.content)
print l
'''
s=re.findall('({.*?})',ret.content)[0]
#print s
data= json.loads(s)

su  = base64.b64encode(urllib.quote("gangsailian@sina.com"))
servertime = data['servertime']
nonce      = data['nonce']
pubkey     = data['pubkey']
rsakv      = data['rsakv']

#####sp
rsaPublickey= int(pubkey,16)
key = rsa.PublicKey(rsaPublickey,65537)
message = str(servertime) +'\t' + str(nonce) + '\n' + str("64158330")
sp = binascii.b2a_hex(rsa.encrypt(message,key))

postdata = {
                    'entry': 'weibo',
                    'gateway': '1',
                    'from': '',
                    'savestate': '7',
                    'userticket': '1',
                    'ssosimplelogin': '1',
                    'vsnf': '1',
                    'vsnval': '',
                    'su': su,
                    'service': 'miniblog',
                    'servertime': servertime,
                    'nonce': nonce,
                    'pwencode': 'rsa2',
                    'sp': sp,
                    'encoding': 'UTF-8',
                    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                    'returntype': 'META',
                    'rsakv' : rsakv,
                    }
url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)'
resp = session.post(url_login,data=postdata)
#print resp.content
print "-------------------------------------------------------"
login_url = re.findall('replace\("(.*)"\)',resp.content)
#print login_url
resp = session.get(login_url[0])
#print resp.content

uid = re.findall('"uniqueid":"(\d+)",',resp.content)[0]

#headers=resp.headers
content="‘失败的原因只有一东西来看待种那就是不够努力’。发现这句话不严谨比如：感情."
def add_new(content,resp):
    add_url  = "http://weibo.com/aj/mblog/add?_wv=5&__rnd=%s770"% int(time.time())
    add_data = {
                'text':content,
                'rank':0,
                'rankid':'',
                'location':'home',
                'module':'stissue',
                "hottopicid":"",
                '_surl':'',
                'pic_id':'',
                '_t':0,
                }
    headers={}
    headers ['set-cookie']= resp.headers['set-cookie']
    headers['Referer'] = 'http://weibo.com/u/'+uid+'?topnav=1&wvr=5'
    resp = session.post(add_url,data=add_data,headers=headers)
    print resp.status_code
add_new(content,resp)        
forwardurl = "http://weibo.com/p/aj/mblog/forward?domain=100505&__rnd=%s"% int(time.time())
def forward(mid,content):
        forwardurl = "http://weibo.com/p/aj/mblog/forward?domain=100505&__rnd=%s"% int(time.time())
        data = {'mid':mid, 'style-type':1, 'reason':content, 'rank':0, 'location':'mblog', '_t':0}
        headers = {}
        headers['set-cookie'] = resp.headers['set-cookie']
        headers['Referer'] = 'http://weibo.com/u/'+uid+'?topnav=1&wv=5'
        respon = session.post(forwardurl, data, headers=headers)
        print respon.status_code
#forward('3632948693565697', forwardurl)   
