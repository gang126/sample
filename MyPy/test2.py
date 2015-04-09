#coding: utf-8
import requests
import zipfile
import os
import shutil


#print "downloading with requests"
#r = requests.get('http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip')
#with open("code3.zip", "wb") as code:
#    code.write(r.content)
#    
#z= zipfile.ZipFile('code3.zip', mode='r') 
#
#for file in z.namelist():
#    z.extract(file,"temp/")
    
zip1= zipfile.ZipFile('f:/test/jeap.zip', mode='r') 

for file in zip1.namelist():
    zip1.extract(file,"f:/test/html5/")       
    
zip2= zipfile.ZipFile('f:/test/blog.zip', mode='r') 

for file in zip2.namelist():
    zip2.extract(file,"f:/test/blog/")

shutil.rmtree("f:/test/html5/jeapblog")     
shutil.copytree("f:/test/blog/jeapblog/", "f:/test/html5/jeapblog/")

shutil.rmtree("f:/test/blog")    
    