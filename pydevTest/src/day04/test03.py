#coding:utf-8
import pygtk
import gobject
import gtk
e      = 0
count  = 1
isexit = 0
def destroy(widget,data=None):
        gtk.main_quit()
def timer_cb():
        global count
        if isexit == 1:
                return
        count +=1
        e.set_text(str(count))
        gobject.timeout_add(100,timer_cb)
        
def button1(widget,data=None):
        global isexit
        if data == 'start':
                isexit = 0
                gobject.timeout_add(100,timer_cb)
        else:
                isexit = 1
                e.set_text('stop')
class app:
        def __init__(self):
                window = gtk.Window(gtk.WINDOW_TOPLEVEL)
                self.window = window
                self.window.set_border_width(10)
                self.window.set_default_size(400,10)
                window.connect("destroy",destroy)
        def newhbox(self):
                self.box1 = gtk.HBox(False,0)
                self.box2.pack_start(self.box1,True,True,0)
        def newvbox(self):
                self.box2 = gtk.VBox(False,0)
                self.window.add(self.box2)
        def newbutton(self,name,cbevent):
                b = gtk.Button(name)
                b.connect('clicked',cbevent,name)
                self.box1.pack_start(b,True,True,0)
                b.show()
        def newentry(self):
                global e
                e = gtk.Entry()
                self.box2.pack_start(e,True,True,0)
                e.show()
w = app()
w.newvbox()
w.newentry()
w.newhbox()
w.newbutton(u"start",button1)
w.newbutton(u"stop",button1)
w.box1.show()
w.box2.show()
w.window.show()
gtk.main()