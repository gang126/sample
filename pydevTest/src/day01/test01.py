import MySQLdb

import random
r=random.randint(1,100)
print(r)

min=1
max=100
while 1:
    i= input("Please input:")
    
    i= int(i)
    
    if i>r:
        max=i
    if i<r:
        min=i
    if i==r:
        print ("You win!" )
        break
    print ("%s----%s"  % (min,max))
        
        
        
    