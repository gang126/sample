#encoding=utf-8
import re
import os
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
b=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
b.get("http://web2.qq.com/webqq.html")

time.sleep(3)
b.find_element_by_xpath('//*[@id="alloy_icon_app_50_3_img"]').click()

time.sleep(3)

b.switch_to_frame('ifram_login')
b.find_element_by_xpath('//*[@id="u"]').clear()
b.find_element_by_xpath('//*[@id="u"]').send_keys('172671026')
b.find_element_by_xpath('//*[@id="p"]').send_keys('p@ssw0rd001')

code=raw_input("please input code ...")
b.find_element_by_xpath('//*[@id="verifycode"]').send_keys(code)
b.find_element_by_xpath('//*[@id="login_button"]').click()
#b.close()

