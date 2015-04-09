import re

print re.search('a(b|c|bc)d','abcd')

print re.search('[0-9a-f]','saswq1234')

print re.findall('fds(.)','fds;fdsa;fdsa;fdsa')

print re.findall('fds(.*)','fds;fdsa;fdsa;\nfdsa')

print re.findall('fds(.*)fds','fds0;fds1;fds2;fds3')

print re.findall('fds(.*?)','fds0;fds1;fds2;fds3')

print re.findall('fds(.+?)','fds0;fds1;fds2;fds3;fds4')

print re.findall('ds(.+?)[f]','fds0;fds1;fds2;fds3;fds4')

print re.search('ds(.*?)','ds')

print re.findall('([\w+@])','ds')