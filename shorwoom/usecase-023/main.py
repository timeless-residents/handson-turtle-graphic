import turtle
import math

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # アニメーションを手動更新モードに

star = turtle.Turtle()
star.shape("turtle")
star.color("yellow")
star.penup()

# 星の初期位置と回転角度
angle = 0


def animate():
    global angle

    # 星の位置と角度を更新
    angle += 5
    x = 200 * math.cos(math.radians(angle))
    y = 200 * math.sin(math.radians(angle))

    star.clear()  # 星の軌跡だけをクリア
    star.goto(x, y)
    star.setheading(angle)

    # 画面を更新
    screen.update()

    # 次のフレームをスケジュール
    screen.ontimer(animate, 50)  # 50ミリ秒後に再実行


# アニメーションを開始
animate()

screen.mainloop()
