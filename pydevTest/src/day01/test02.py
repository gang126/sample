import random

s='hello'

l1=list(s)

l2=[]

# l3=l1[::-1]
# print(l3)


# while len(l1)>0:
#     
#     l2.append(l1.pop())
#     
# print(l2)


# for i in l1[:]:
#     l2.append(l1.pop())
#     
# print(l2) 


# for n in range(len(l1)-1,-1,-1):
#     print(l1[n])


# while len(l1)>0:
#     l2.insert(len(l2), l1.pop())
# print(l2)


l4=[1,2,3,4,5]
print(l4) 
l5=[]
while(len(l5)!=len(l4)):
    ran=random.randint(1,5)
    if ran not in l5:
        l5.append(ran)
print(l5)    
    



