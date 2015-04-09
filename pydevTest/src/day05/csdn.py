#encoding=utf-8
import requests
import getpass

pw=getpass.getpass()

login_url='https://passport.csdn.net/ajax/accounthandler.ashx'

######
data= {'t':'log',
       'u':'gangsailian',
       'p':pw,
       'remember':'0',
       'f':'http://www.csdn.net/',
       'rand':'0.3277420655358583',
       }


headers={
         'Host':'passport.csdn.net',
         'Referer':'https://passport.csdn.net/account/loginbox?callback=logined&hidethird=1&from=http%3a%2f%2fwww.csdn.net%2f',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36',
         }
######
session =requests.Session()
ret=session.get(login_url, data=data, headers=headers)

# ret=session.get('http://www.csdn.net')
# print ret.content
#http://blog.csdn.net/qsyzb/article/details/12113991

def comment(user, id,content):
    blog_comment='http://blog.csdn.net/%s/comment/submit?id=%s'
    blog_comment=blog_comment%(user,id)

    headers={
             'Host':'blog.csdn.net',
             'Origin':'http://blog.csdn.net',
             'Referer':'http://blog.csdn.net/%s/article/details/%s'%(user,id),
             'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36',
}

    data={
          'commentid':'',
          'content':content,
          'replyId':'',
}
    ret=session.post(blog_comment, data=data,headers=headers)
    #print ret.content

comment('fansongy','12111581','me too')    