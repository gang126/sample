#encoding=utf-8
import urllib2

# url="http://www.jeapedu.com"
# 
# f=urllib2.urlopen(url)
# 
# #print f.read()
# 
# print dir(f)
# 
# print f.headers.keys()
# print f.headers.values()
######################################url
# url1="http://www.baidu.com/s?wd=%s"%("python")
# 
# url="http://www.baidu.com/s?wd=%s"
# f=urllib2.urlopen(url%(''))
# print f.read()

#url%('python')

###################################编码

s1="你好"
s2= u'你好 '

#print s1.decode('gb2312').encode('utf-8')

print s2.encode('utf8')




