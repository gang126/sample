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

for k,v in d.items():
    if r1 in v:
        sk=k
    if r2 in v:
        ek=k 

####3.  375 �� 387 ��ͬվ����   ѧԺ·

for i in d[sk]:
    if i in d[ek]:
        print (sk, i, ek)  
#########################
# l=list(set(d[sk])& set(d[ek]))
# 
# for i in l:
#     print(i)


