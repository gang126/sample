#coding=utf8
import pygtk
import gtk

def destroy(widget, data=None):
    gtk.main_quit()
    
def button1(widget,data=None): 
    print "hello %s" % data      
    
class app:
    def __init__(self):
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy",destroy)
        self.window=window
        self.window.set_border_width(10)
        self.window.set_default_size(400,10)

    def newbox(self):
        self.box1=gtk.HBox(False,10)
        self.window.add(self.box1)
                
    def newbutton(self,name,cbvent):
        self.b=gtk.Button(name)
        self.b.connect('clicked',cbvent,name)
        #self.window.add(self.b)
        self.box1.pack_start(self.b,True,True,0)
        self.b.show()
    
        
w=app()
#w.button("按钮",button1)
w.newbox()
w.newbutton(u"1",button1)
w.newbutton(u"2",button1)
w.box1.show()

w.window.show()
gtk.main()