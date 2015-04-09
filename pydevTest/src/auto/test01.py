#encoding=utf-8
import logging
from selenium import webdriver

logging.basicConfig(filename = "log1005", level = logging.DEBUG)
b=webdriver.Firefox()
b.get("http://www.cpython.org")


links=b.find_elements_by_tag_name('a')

# b.find_element_by_link_text("视频").click()
# b.find_element_by_link_text("python基础").click()
count=1
for l in links:
    n=b.execute_script("var d=document,a=d.createElement('a');a.target='_blank';a.href=arguments[0];a.innerHTML='.';d.body.appendChild(a);return a", l)
    href = n.get_attribute('href')
    if href.find('mailto:') > -1:
        continue
    
    n.click()
    import time
    time.sleep(1)
    b.switch_to_window(b.window_handles[-1])
    b.get_screenshot_as_file(str(count)+'.png')
    b.close()
    count +=1
    b.switch_to_window(b.window_handles[0])
    
    
    
        