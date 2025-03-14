import turtle


def draw_fractal(turtle_instance, length, depth):
    if depth > 0:
        for i in range(3):
            turtle_instance.forward(length)
            draw_fractal(turtle_instance, length / 2, depth - 1)
            turtle_instance.backward(length)
            turtle_instance.right(120)


turtle_instance = turtle.Turtle()
turtle_instance.speed(0)  # 最速で描画する
draw_fractal(turtle_instance, 100, 3)

turtle.done()
