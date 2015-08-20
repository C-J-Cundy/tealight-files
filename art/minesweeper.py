from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

def draw_grid(x,y,size):
  for i in range(10):
    for j in range(10):
      box(x+i*size,y+j*size,size,size)
      color("white")
      box(x+size/10+i*size,y+size/10+j*size,size/10*8,size/10*8)
      color("black")
    
draw_grid(50,50,80)

def handle_mousedown(x,y):
  print x,",",y