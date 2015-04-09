# coding=gbk
from __future__ import with_statement
import fileinput 
import ConfigParser 
import time

print time.strftime("%Y-%m-%d %H:%M:%S")

def content():
    num=0
    for line in fileinput.input("file", inplace=True):
        if num==0:
            x= line
        elif (num>0):
            if line != '\n':
                print line,
        num +=1    
    return x    
#print firstLine()            

config=ConfigParser.ConfigParser()
with open('user','r') as cfgfile:
    config.readfp(cfgfile)
    name=config.get('info','user')
    age=config.get('info','pwd')
    print name
    print age