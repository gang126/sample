#coding= utf-8
from __future__ import with_statement
import fileinput 
import ConfigParser
import requests
import re,time
import json
import urllib
import base64
import rsa
import binascii


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
content=content()

print content

