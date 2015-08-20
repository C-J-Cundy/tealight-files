from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)
import random

size=80
xstart=50
ystart=50
numMines=10

mines = []


def draw_grid(x,y,size):
  for i in range(10):
    for j in range(10):
      box(x+i*size,y+j*size,size,size)
      color("lightblue")
      box(x+size/10+i*size,y+size/10+j*size,size/10*8,size/10*8)
      color("black")      

def setup():
  draw_grid(xstart,ystart,size)
  global mines
  for i in range(10):
    mines.append([])
    for j in range(10):
      mines[i].append(0)
      
  #Make mines
  counter=0
  while(counter < numMines):
    tmpx=random.randint(0,9)
    tmpy=random.randint(0,9)
    if (mines[tmpx][tmpy] != -1):
      mines[tmpx][tmpy] = -1
      counter += 1
      
  #Calculate nums
  for i in range(10):
    for j in range(10):
      if mines[i][j] != -1:
        minescount=0
        for offx in range(-1,2):
          for offy in range(-1,2):
            if i + offx >= 0 and i + offx <= 9 and j+offy >= 0 and j + offy <= 9:
              if mines[i+offx][j+offy] == -1:
                minescount += 1
        mines[i][j] = minescount
          
          
def reveal(i,j):
  if mines[i][j] == -1:
    print "You lose"
  tx=xstart+size/10+i*size
  ty=xstart+size/10+j*size
  color("white")
  box(tx,ty,size/10*8,size/10*8)
  color("black")
  text(tx+size/10*3,ty+size/10*3,mines[i][j])
  
  
setup()
print mines

def handle_mousedown(x,y):
  global mines
  boxX=(x-xstart)/size
  boxY=(y-ystart)/size
  print boxX,",",boxY,",",mines[boxX][boxY]
  if boxX >= 0 and boxY >= 0 and boxX <= 9 and boxY <= 9:
    reveal(boxX,boxY)