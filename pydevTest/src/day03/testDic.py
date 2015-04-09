# coding=gbk

#-----------1. 生成字典
d={}

f=open("dict")

while 1:
    line=f.readline()
    if line:
        d1=line.split(":")
        d[d1[0]]=d1[1]
        
    else:
        break    
print(d)

#-----------2. 做输入匹配
r=input("please input:")

if d.get(r):
    print(d.get(r))
else:
    print("no value")
    
    