import turtle

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.right(90)

turtle.done()  # 描画を完了し、ウィンドウを維持する
