
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
    canv.delete('hjbh1','hjbh2')
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0, tag = 'hjbh1')
    root.after(1000, new_ball)
  
    canv.create_text(200, 100, text = ('Score:', n) , justify=CENTER, font="Verdana 14", tag = 'hjbh2')
def randomizer():
    a = [rnd(-10,10), rnd(-10, 10), choice(colors)]
    return a
xr = randomizer()[0]
yr = randomizer()[1]
zr = randomizer()[2]
class Ball:
    def __init__(self, x1, y1, r1):
        self.x1 = x1
        self.y1 = y1
        self.r1 = r1
        
               
    def move(self):
        if 
        canv.delete('hjbhi1')
        self.x1 += xr 
        self.y1 += yr
        canv.create_oval(self.x1 - self.r1, self.y1 - self.r1, self.x1 + self.r1, self.y1 + self.r1, fill = zr, width = 0, tag = 'hjbhi1')
        root.after(22, ball.move)


 

def click(event):   
    global n
    if not ((event.x - x)**2 + (event.y - y)**2)**0.5 > r:
        n +=1
ball = Ball(rnd (100, 700), rnd(100, 500), rnd(10, 30))
ball.move()
new_ball()
canv.bind('<Button-1>', click)
mainloop()

