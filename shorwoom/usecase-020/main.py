import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("散布図")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_scatter_plot(data):
    # 軸の描画
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    pen.forward(400)  # x軸
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.left(90)
    pen.forward(400)  # y軸
    pen.right(90)

    for x, y, label in data:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.dot(5, "blue")  # 点を描画
        # ラベルを付ける (オプション)
        # pen.write(label, align="left")


data = [(50, 80, "A"), (120, 30, "B"), (80, 150, "C"), (180, 100, "D")]

draw_scatter_plot(data)

screen.mainloop()
