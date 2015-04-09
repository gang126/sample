
# f=open("file")
# print f.read()
# f.close()

# with open("file") as f:
#     print f.read()
    
    
class WITH_TEST:
    def __init__(self,filename):
        self.filename=filename
    
    def __enter__(self):
        self.f=open(self.filename) 
        return self.f
    
    def __exit__(self,type,msg,traceback):
        print "file %s close" % self.filename    
        self.f.close()
        
        
with WITH_TEST('file') as f:
    print f.readline()
            