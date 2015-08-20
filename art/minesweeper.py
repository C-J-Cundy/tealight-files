from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

size=80
xstart=50
ystart=50

mines = [[]]


def draw_grid(x,y,size):
  for i in range(10):
    for j in range(10):
      box(x+i*size,y+j*size,size,size)
      color("white")
      box(x+size/10+i*size,y+size/10+j*size,size/10*8,size/10*8)
      color("black")

def setup():
  draw_grid(xstart,ystart,size)
  global mines
  for i in range(10):
    for j in range(10):
      mines[i].append(0)

setup()
print mines

def handle_mousedown(x,y):
  global mines
  boxX=(x-xstart)/size
  boxY=(y-ystart)/size
  print boxX,",",boxY