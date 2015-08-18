from tealight.logo import move, turn


def lines(length, number, spacing):
     for i in range(0,number):
        move(length)
        turn(90)
        move(spacing)
        turn(90)
     turn(90)
     move(spacing*number)

lines(100,100,100)

