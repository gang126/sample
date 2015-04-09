#encoding=utf-8
import requests
 
session= requests.Session()
url='http://uliweb.cpython.org/login'
ret=session.get(url)
 
csrf_token= ret.headers['set-cookie'].split(';')[0].split("=")[1]
next='http://uliweb.cpython.org/forum'
data={'csrf_token':csrf_token,
      'username':'larryzheng',
      'password':'64158330',
      'next':next
      }
 
session.post(url, data)
 
############
url_post='http://uliweb.cpython.org/forum/2/new_topic'
ret=session.get(url_post)
 
slug= ret.content.split('name="slug"')[1].split("><")[0].split("value=")[1]
print slug
slug=slug[1:-1]
print slug
 
post_data={'csrf_token':csrf_token,
           'subject':'hello larry 0.0',
           'content':'python test',
           'slug':slug,
           'enable_comment':'on'
           }
ret=session.post(url_post,post_data)
print ret.content

#########

    


