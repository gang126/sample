#encoding=utf-8
from selenium import webdriver

b=webdriver.Firefox()
b.get("http://www.cpython.org")


links=b.find_elements_by_tag_name('a')

# b.find_element_by_link_text("视频").click()
# b.find_element_by_link_text("python基础").click()
# l1=[]
# for l in links:
#     l1.append(l)
    
l1 = list(links)

for i in links:
    print i.text
    i.click()
    import time
    time.sleep(1)
    b.back()
    #b.current_window_handle()
    
        
    
    
    
        