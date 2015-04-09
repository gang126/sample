#1-1000

import random
d1={}



l1=[]
for i in range(1,11):
    l1.append(i) 
    
print(l1)   

count=1
while 1:
        
    key=random.randint(0,9)
#     print(key)
#     d1[l1.pop(key)]=count
#     count+=1
    if d1.get(l1[key])==None:
        d1[l1[key]]=count
        count+=1
    if count==10:
        break     

print(d1)    
    


