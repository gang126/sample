# coding=gbk

#-----------1. �����ֵ�
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

#-----------2. ������ƥ��
r=input("please input:")

if d.get(r):
    print(d.get(r))
else:
    print("no value")
    
    