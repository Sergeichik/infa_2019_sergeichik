
from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
n = 0
def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    root.after(1000, new_ball)
  
    canv.create_text(200, 100, text = ('Score:', n) , justify=CENTER, font="Verdana 14")
x1 = rnd(100, 700)
y1 = rnd(100, 500)
r1 = rnd(30, 50)

    def rand_ball():
    global x1, y1, r1
    canv.delete('hijbh')
    xr = rnd(-10, 10)
    yr =rnd(-10, 10)
    x1 += xr
    y1 += yr  
    canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill = choice(colors), width = 0, tag = 'hijbh')
    root.after(2, rand_ball) 

 

def click(event):   
    global n
    if not ((event.x - x)**2 + (event.y - y)**2)**0.5 > r:
        n +=1

   
new_ball()
canv.bind('<Button-1>', click)
rand_ball()
mainloop()
