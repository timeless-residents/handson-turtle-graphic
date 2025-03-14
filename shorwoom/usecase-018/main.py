import turtle

# スクリーンオブジェクトを作成
screen = turtle.Screen()
screen.setup(width=800, height=600)  # 画面サイズを設定
screen.bgcolor("white")  # 背景色を設定
screen.title("棒グラフ")  # ウィンドウタイトルを設定

# タートルオブジェクトを作成
pen = turtle.Turtle()
pen.speed(0)  # 描画速度を最速に設定
pen.hideturtle()  # タートルアイコンを非表示


def draw_bar(height, label, color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(90)
    pen.forward(height)
    pen.write(label, align="center")  # ラベルを追加
    pen.right(90)
    pen.forward(40)
    pen.right(90)
    pen.forward(height)
    pen.left(90)
    pen.end_fill()


data = [("A", 100, "red"), ("B", 150, "green"), ("C", 80, "blue"), ("D", 120, "orange")]

x_start = -150  # グラフの開始位置を調整

pen.penup()
pen.goto(x_start, -100)  # グラフの開始位置を設定
pen.pendown()

for label, value, color in data:
    draw_bar(value, label, color)

screen.mainloop()  # 画面を維持
