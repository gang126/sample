import random


# l1=list('abcdefghijklmnopqrstuvwxyz')
# 
# print(l1)
# 
# l2=[]
# 
# while len(l2)!=len(l1):
#     i=random.randint(0,len(l1)-1)
#     x=l1[i]
#   
#     if x not in l2:
#         l2.append(x)
#         
# print(l2)   

l1=[]
for i in range(1,111):
    l1.append(i) 
    
print(l1)    

l2=[]
while (len(l1)!=0):
    i=random.randint(0,len(l1)-1)   
    l2.append(l1.pop(i))    
        
print(l2)        