# coding=gbk

###1.  375 ��ֱ��---ѧԺ·---387----������վ    ##375��������ֱ��
      
f=open("busTrans")
d={}
while 1:
    line=f.readline().strip()
    if line:
        d1=line.split(":")
        d[d1[0]]=d1[1].split(",")
    else:
        break
print(d)        

r1=input("from:")
r2=input("to:")

for i in d.keys():
    if r1 in d.get(i):
        fro=i
        #print(fro)                          

####2. 387�����˱�����վ

for i in d.keys():
    if r2 in d.get(i):
        des=i
        #print(des)
         
#print(fro)         
#print(des)

####3.  375 �� 387 ��ͬվ����   ѧԺ·

flag=0
for i in d.get(fro):
    if i in d.get(des):
        mid=d.get(fro)[flag]
        print(fro,mid,des)  
    flag +=1
 
#print(fro,mid,des)        

l=[]