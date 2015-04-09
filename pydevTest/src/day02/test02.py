

i=input("please input:")

if i.find("+")>0:
    l1=i.split("+")
    sum=int(l1[0])+int(l1[1])
if i.find("-")>0:
    l1=i.split("-")
    sum=int(l1[0])-int(l1[1])
if i.find("*")>0:
    l1=i.split("*")
    sum=int(l1[0])*int(l1[1])
if i.find("/")>0:
    l1=i.split("/")
    sum=int(l1[0])/int(l1[1])        
print(sum)