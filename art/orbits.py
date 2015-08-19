from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.3


def handle_keydown(key, power):
  global ax, ay
  
  if key == "left":
    if power > 0:
      ax = -power
      power -= 0.01
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  #ay += (1 * 10 ** -3) #Gravity in -Y direction

  spot(x,y,8)
  
  
