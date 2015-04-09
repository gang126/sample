

f=open("user","r+")

line=f.readlines()

n=0
while n<len(line):
    
    if "pwd" in line[n]:
        line[n]="xxx"
    print line[n]    
    n+=1    
g=open("user","w+")
g.writelines(line) 
