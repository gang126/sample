# coding=gbk

#-----------1. 生成字典
# d={}
# 
# f=open("dict")
# 
# r=input("please input:")
# 
# while 1:
#     line=f.readline()
#     if line:
#         d1=line.split(":")
#         if r==d1[0]:
#             print(d1[1])  
#         
#     else:        
#         break    

#######################################

f=open("dict")
l=[]
while 1:
    line=f.readline()
    if line:
        d=line.split(":")
        l.append(d)
    else:
        break
print(l)        

r=input("please input:")

for i in l:
    if r==i[0]:
        print(i[1])

    