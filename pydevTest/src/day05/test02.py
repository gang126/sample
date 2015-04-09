#encoding=utf-8
import requests

session= requests.Session()
url='http://uliweb.cpython.org/login'
ret=session.get(url)

# ret.status_code
# ret.content[3908:].find('csrf_token')
# 
# print ret.headers
# print ret.content[4264+3908:]

csrf_token= ret.headers['set-cookie'].split(';')[0].split("=")[1]
next='http://uliweb.cpython.org/forum'
data={'csrf_token':csrf_token,
      'username':'python',
      'password':'python',
      'next':next
      }

session.post(url, data)
ret=session.get(next)

print ret.content
