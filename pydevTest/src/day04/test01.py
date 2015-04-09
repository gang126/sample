#coding: utf-8
import gtk


def click_button(widget, data=None):
    print("click_button")
    
def de(widget,data=None):
    gtk.main_quit() 
       
w=gtk.Window()
w.set_default_size(400,300)
w.connect("destroy",de)

vb=gtk.VBox(False,0)
w.add(vb)
vb.show()

b=gtk.Button("确定1")
b.connect('clicked', click_button,None)

w.add(b)
b.show()

b=gtk.Button("取消")
b.connect('clicked', click_button,None)
vb.pack_start(b,True,True,0)
b.show()