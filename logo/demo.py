from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,300):
  move(2*i)
  turn(90.02)
  color(colors[i%3])