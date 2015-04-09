import random
l1=[2,1,0,3,4]
l2=['a','b','c','d','e']
l3=['abc','de','fgh','ijklm','nopqrst','uvwxyz']
#l4=[0,3,5,8,13,20]

f=open('file','r+')

# i=0
# while(i<len(l1)):
#     word=l2[l1[i]]
#     f.seek(l1[i])
#     print(f.tell())
#     f.write(word) 
#     i+=1
#     
# f.close()  

# i=0
# while(i<len(l2)):
#     ran=random.randint(0,len(l2)-1)  
#     word=l2[ran]
#     f.seek(ran)
#     print(f.tell())
#     f.write(word)
#     i+=1
#     
# f.close()    



i=0
l4=[0]

for j in l3:
    l=l4[-1]+ len(j)
    l4.append(l)  

print(l4)        
    
while(i<len(l3)):
        ran=random.randint(0,len(l3)-1)  
        word=l3[ran]
        f.seek(l4[ran])
        print(f.tell())
        f.write(word)
        i+=1
    
    
f.close()    