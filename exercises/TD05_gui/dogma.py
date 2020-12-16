from tkinter import*
from random import randint 
root=Tk()
root.title("dégradé aléatoire")
 
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
 
def RGB(r,v,b):
     return "#%02x%02x%02x" % (r,v,b)
 
can = Canvas(root,height=255,width=255)
can.pack(side=BOTTOM)
 
for i in range(255):
        color=get_color(randint(0, 255), randint(0, 255), randint(0, 255) )
        can.create_line(0,i,255,i,width=1,fill=color)
 
mainloop() 