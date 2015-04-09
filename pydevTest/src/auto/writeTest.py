l=[1111,2222,3333,4444]
f = open('weiboId.txt', 'a+')

i=0
while(i<len(l)):
    f.write(str(l[i])+",")
    i+=1
    
    
f.close()    

#f = open('weiboId.txt', 'r')
#
#while 1:
#    line=f.readline()
#    if line:
#        list=line.split(",")
#        print len(list)
#        for i in list:
#            print i
#    else:
#        break    
#f.close()    