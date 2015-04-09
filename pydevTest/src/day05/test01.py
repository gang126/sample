import urllib2
import sys

#url="http://www.baidu.com/s?wd=%s"

url="http://blog.csdn.net"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'}

#f=urllib2.urlopen(url%(sys.argv[1]))

request=urllib2.Request(url,headers=headers)


f=urllib2.urlopen(request)
print f.read()


