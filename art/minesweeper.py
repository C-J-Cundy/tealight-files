from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

def draw_grid(x,y):
  for i in range(10):
    for j in range(10):
      box(0,0,100,100)
    
draw_grid(0,0)