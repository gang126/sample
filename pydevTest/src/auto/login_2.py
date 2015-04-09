#coding: utf-8
import webbrowser
from weibo import APIClient

APP_KEY = '1373808687' # app key
APP_SECRET = '139aa621dfc1529c8f8bfa132962c2dc' # app secret
CALLBACK_URL = 'http://127.0.0.1:8000' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

webbrowser.open(url)
code = your.web.framework.request.get('code')
code="d1eb2816fe88c9f501958a4afbeb55d8"

r = client.request_access_token(code)
access_token = r.access_token
print access_token
expires_in = r.expires_in 
#2.00B1b33Cd53yUBdae751f1402IyNaDs
client.set_access_token(access_token, expires_in)
print client.users.show.get(access_token=access_token,screen_name='sunislee')
#print client.statuses.user_timeline.get()
#print client.statuses.update.post(status=u'发布微博')
#print client.statuses.upload.post(status=u'发微博', pic=open('C:\\Users\ssHss\\Desktop\\test.png'))
#client.statuses.repost.post(id=3632948693565697,status=u'xxxxxx')