import turtle
import random

# 画面の作成
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightgreen")
screen.title("タートルレース")

# レーサーとなるタートルをリストで管理
turtles = []
colors = ["red", "blue", "orange", "purple"]  # 好きな色に変更可能
start_positions = [-150, -100, -50, 0]  # スタート地点のY座標

# レーサーの初期化と配置
for i in range(4):
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color(colors[i])
    pen.penup()
    pen.goto(-250, start_positions[i])  # X座標は固定で、Y座標をずらす
    turtles.append(pen)
    pen.speed(0)  # アニメーション速度を最速に

# ゴールの描画
goal_line = turtle.Turtle()
goal_line.penup()
goal_line.goto(250, 180)
goal_line.pendown()
goal_line.goto(250, -180)
goal_line.hideturtle()  # ゴールラインのタートルは非表示にする

# レースの開始
is_race_on = True
while is_race_on:
    for turtle in turtles:
        # ランダムな距離だけ前進
        distance = random.randint(1, 10)
        turtle.forward(distance)

        # ゴールに到達したか確認
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(f"{winning_color}色のタートルが勝ちました！")
            break

# ゲーム終了時に画面をクリックすると終了するようにする
screen.exitonclick()
