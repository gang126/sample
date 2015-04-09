# coding=gbk

import test01 as b

b.myadd1(4,3)

print("----------------------------------")
########################

class A:
    def __init__(self,n):
        self.name=n
        
    def __del__(self):
        print("bye")    
        
a1= A('larry')
print(a1.name)        
#a1=11

print(dir(a1))

print("-------------------------")
#######继承
# class B(A):
#     pass
# 
# b1=B("bbb")
# print(dir(b1))


