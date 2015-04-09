# coding=gbk

###1.  375 西直门---学院路---387----北京西站    ##375包含了西直门
      
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

####2. 387包含了北京西站

for i in d.keys():
    if r2 in d.get(i):
        des=i
        #print(des)
         
#print(fro)         
#print(des)

####3.  375 和 387 相同站点是   学院路

flag=0
for i in d.get(fro):
    if i in d.get(des):
        mid=d.get(fro)[flag]
        print(fro,mid,des)  
    flag +=1
 
#print(fro,mid,des)        

l=[]