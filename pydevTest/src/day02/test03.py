# f=open('file',"r+") 
# 
#  
# f.write("1\n")
#  #f.write("l")
# f.close()


# f.seek(1)
# f.write('c')
# 
# print(f.tell())


############################################
l1=[0,1,2,3,4,5,6,7,8,9]
 
f=open('file','r+')
 
i=0
while (i<len(l1)):
    f.write(str(l1[i]))
    i+=1
f.close()
     
    