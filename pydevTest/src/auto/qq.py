#encoding=utf-8
import time
import os
from selenium import webdriver

b=webdriver.Firefox()
b.get("http://web2.qq.com/webqq.html")

i=20
while i>0:
    a=b.find_elements_by_css_selector('div.EQQ_BuddyList_Nick')
    if a.__len__()>0:
        a[0].click()
        b.find_element_by_css_selector('div.rich_editor_div').send_keys('python')
        b.find_element_by_css_selector('a.chatBox_sendMsgButton').click()
        b.find_elements_by_css_selector("a.ui_button.window_action_button.window_close")[1].click()
        break
    print "wait..."
    time.sleep(1)
   

