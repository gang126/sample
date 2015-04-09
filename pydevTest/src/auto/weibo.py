#encoding=utf-8
import re
import time
import requests
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# b=webdriver.Chrome(chromedriver)
# b.get("http://www.baidu.com")

b=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
b.get("http://apps.weibo.com/tuituoo?ref=appsearch")
raw_input("please...")
#b.get("http://apps.weibo.com/tuituoo")
#time.sleep(20)

all_cookies = b.get_cookies()
cookies = {}
for s in all_cookies:
    cookies[s['name']] = s['value']
    
#ret = requests.get('http://tuitu.sinaapp.com/weibo/task/followtuis/p/1/province/0/city/0',cookies=cookies)
#re.findall('tu_follow\((\d+), this',ret.content)

access_token='2.00B1b33CpQpX8E22629dcf17IzqRpB'
source='4071554311'


def follow(sid):
    url1='http://tuitu.sinaapp.com/weibo/task/dofollow'
    url2='https://api.weibo.com/2/friendships/create.json'
    url3='http://tuitu.sinaapp.com/weibo/task/followsuccess'
    ret1=requests.post(url1,data={'sid':sid},cookies=cookies)
    ret2=requests.post(url2,data={'source':source,'uid':sid,'_cache_time':'0','method':'post','access_token':access_token},cookies=cookies)
    ret3=requests.post(url3,data={'sid':sid},cookies=cookies)

def unfollow(sid):
    url4='https://api.weibo.com/2/friendships/destory.json'
    ret4=requests.post(url4,data={'source':source,'uid':sid,'_cache_time':'0','method':'post','access_token':access_token},cookies=cookies)

def getsid():
    ret5 = requests.get('http://tuitu.sinaapp.com/weibo/task/followtuis/p/1/province/0/city/0',cookies=cookies)
    allid=re.findall('tu_follow\((\d+), this',ret5.content)
    for i in allid:
        follow(i)
        #addfollow(i)
        print i
getsid()        


     

