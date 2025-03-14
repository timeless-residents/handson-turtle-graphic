import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic animation

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

# ボールの初期位置と速度
x, y = 0, 0
dx, dy = 2, 3

# アニメーション関数
def animate():
    global x, y, dx, dy
    
    # 位置を更新
    x += dx
    y += dy

    # 壁との衝突判定
    if x > 290 or x < -290:
        dx *= -1
    if y > 290 or y < -290:
        dy *= -1

    # ボールを移動
    ball.goto(x, y)
    
    # 画面を更新
    screen.update()
    
    # 次のフレームをスケジュール
    screen.ontimer(animate, 10)  # 10ms待機

# アニメーション開始
animate()

# イベントループを開始
screen.mainloop()
