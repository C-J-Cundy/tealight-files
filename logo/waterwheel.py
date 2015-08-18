from tealight.logo import move, turn


def lines(length, number, spacing):
     for i in range(0,number/2):
        move(length)
        turn(90)
        move(spacing)
        turn(90)
        move(length)
        
     turn(90)
     move(spacing*number)

lines(100,10,10)

