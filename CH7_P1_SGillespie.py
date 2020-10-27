from turtle import Turtle

def main():
    t = Turtle()
    drawCircle(t, 10, 10, 20)

def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * 3.1415*radius/120.0)

main()
