from tealight.logo import move, turn

def chessboard(number, length, spacing):
  for i in range(0,number):
    turn(90)
    move(i*spacing)
    turn(-90)
    move(length)
    turn(-180)
    move(length)
    turn(90)
    move(i*spacing)
    turn(90)
 
  move(length)
  turn(90)
  for i in range(0,number):
    turn(90)
    move(i*spacing)
    turn(-90)
    move(length)
    turn(-180)
    move(length)
    turn(90)
    move(i*spacing)
    turn(90)
  
  
    
chessboard(9,160,20)