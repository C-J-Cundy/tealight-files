from tealight.logo import move, turn


def lines(length, number, spacing):
     for i in range(0,number):
        turn(90)
        move(spacing*i)
        turn(-90)
        move(length)
        turn(180)
        move(length)
        turn(180)
        turn(-90)
        move(spacing*i)
        turn(90)

lines(100,10,10)

