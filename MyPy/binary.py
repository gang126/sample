

x=raw_input("please input");


def toBinary(x):
    while x>=1:
        y=x%2
        x=x/2
        print y
        
#toBinary(int(x))        

def toEight(x):
    while x>=1:
        y=x%8
        x=x/8
        print "8 hexadecimal: ",y
#toEight(int(x))  


#24054541724=> 0xa1b2c3d4

def toHex(x):
    while x>=1:
        y=x%16
        if y==10:
            y="a"
        elif y==11:
            y="b"
        elif y==12:
            y="c"
        elif y==13:
            y="d"
        elif y==14:
            y="e"
        elif y==15:
            y="f"                   
        x=x/16
        print "16 hexadecimal: ",y

toHex(int(x))






