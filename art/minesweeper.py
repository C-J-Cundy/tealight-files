from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

def draw_grid(x,y):
  for i in range(10):
    for j in range(10):
      box(x+i*100,y+j*100,100,100)
      color("white")
      box(x+20+i*100,y+20+j*100,80,80)
    
draw_grid(100,100)