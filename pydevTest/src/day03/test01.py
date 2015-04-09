
#########
x=[0,1,2,4]

def myadd(a,b):
    x=[1,2,3]
    x[0]=a+b
    
myadd(3,4)    
print(x)    

#############
def myadd1(a, b=10):
    print(a+b)

myadd1(3,1)


##########
def myadd2(a, b=10):
    print(a,b)

myadd2(b=3,a=5)    