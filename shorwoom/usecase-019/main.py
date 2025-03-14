import turtle
import math

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("円グラフ")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_pie_chart(data):
    total = sum(data.values())
    start_angle = 0
    for label, value in data.items():
        angle = (value / total) * 360
        pen.fillcolor(get_color(label))  # 色を動的に決定
        pen.begin_fill()
        pen.goto(0, 0)
        pen.setheading(start_angle)
        pen.circle(100, angle)
        pen.goto(0, 0)
        pen.end_fill()
        start_angle += angle
        # 凡例を追加 (少し工夫が必要)
        x = 150 * math.cos(math.radians(start_angle - angle / 2))
        y = 150 * math.sin(math.radians(start_angle - angle / 2))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.write(f"{label} ({value})", align="center")


def get_color(label):
    # ラベルに基づいて色を決定する簡単な例
    colors = ["red", "green", "blue", "orange", "purple"]
    return colors[hash(label) % len(colors)]

data = {"A": 30, "B": 20, "C": 25, "D": 15, "E": 10}

draw_pie_chart(data)

screen.mainloop()
