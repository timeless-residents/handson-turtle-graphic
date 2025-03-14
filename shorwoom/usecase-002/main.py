import turtle

turtle_instance = turtle.Turtle()

side_length = 50
angle = 60

for i in range(6):
    turtle_instance.forward(side_length)
    turtle_instance.right(angle)

turtle.done()
