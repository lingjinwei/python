import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for x in range(200):
    turtle.forward(2*x)
    turtle.left(200)
time.sleep(3)
