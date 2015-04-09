import sys

class culate():
    #加法
    def add(self,a,b):
        return a+b
    #减法
    def mut(self,a,b):
        return a-b
    #乘法
    def sub(self,a,b):
        return a*b
    #除法
    def mod(self,a,b):
        return a/b

c=culate()
while True:
    n=input("请选择你的操作：\n1.加法\n2.减法\n3.乘法\n4.除法\n0.退出\n")
    if n=="0":
        break
    elif n=="1":
        a=input("请输入第一个数：")
        b=input("请输入第二个数：")
        print(c.add(int(a),int(b)))
        continue
    elif n=="2":
        a=input("请输入第一个数：")
        b=input("请输入第二个数：")
        print(c.mut(int(a),int(b)))
        continue
    elif n=="3":
        a=input("请输入第一个数：")
        b=input("请输入第二个数：")
        print(c.sub(int(a),int(b)))
        continue
    elif n=="4":
        a=input("请输入第一个数：")
        b=input("请输入第二个数：")
        print(c.mod(int(a),int(b)))
        continue
