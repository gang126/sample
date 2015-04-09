#encoding=utf-8
import re
import os
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# b=webdriver.Chrome(chromedriver)
# b.get("http://www.baidu.com")

b=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
b.get("https://wx.qq.com/")
 
raw_input("...")

a=b.find_elements_by_css_selector("a.friendDetail")
for i in a:
    id=i.get_attribute('id')
    print id
    
b.find_element_by_xpath('//*[@id="con_item_wxid_w2i0n53kly1211"]').click()
b.find_element_by_xpath('//*[@id="textInput"]').send_keys('test')
b.find_element_by_xpath('//*[@id="chat_editor"]/div[1]/a').click()

# list=re.findall('"left name".*?>(.*?)</div>',b.page_source())
# for i in list:
#     print i.text
     

