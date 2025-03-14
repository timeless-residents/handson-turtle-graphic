import turtle


def draw_triangle(turtle_instance, side_length):
    for i in range(3):
        turtle_instance.forward(side_length)
        turtle_instance.right(120)


turtle_instance = turtle.Turtle()
draw_triangle(turtle_instance, 100)

turtle.done()
