#encoding=utf-8

import requests
import re

session=requests.Session();
ret=session.get("http://uliweb.cpython.org/forum")
str=ret.content
str=str.split('class="table"')[1]
list=re.findall('<a href=".*?">(.*?)</a>',str)

#print list
index=0
for i in list:
    if (index%2==0):
        print i
    index +=1    
    