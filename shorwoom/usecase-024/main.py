import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# 複数の星を作成
stars = []
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

for i in range(20):
    star = turtle.Turtle()
    star.shape("circle")
    star.color(random.choice(colors))
    star.penup()
    star.goto(random.randint(-290, 290), random.randint(-290, 290))
    star.dx = random.randint(-5, 5)
    star.dy = random.randint(-5, 5)
    stars.append(star)


def animate():
    # 各星を移動
    for star in stars:
        x, y = star.position()

        # 位置を更新
        star.goto(x + star.dx, y + star.dy)

        # 壁との衝突判定と位置調整
        if x > 290:
            star.setx(290)
            star.dx *= -1
        elif x < -290:
            star.setx(-290)
            star.dx *= -1
            
        if y > 290:
            star.sety(290)
            star.dy *= -1
        elif y < -290:
            star.sety(-290)
            star.dy *= -1
            
    # 星同士の衝突判定
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            # 2つの星の距離を計算
            distance = stars[i].distance(stars[j])
            # 距離が小さい場合（衝突と判定）
            if distance < 20:
                # 速度を交換（物理的な反射）
                stars[i].dx, stars[j].dx = stars[j].dx, stars[i].dx
                stars[i].dy, stars[j].dy = stars[j].dy, stars[i].dy

    # 画面を更新
    screen.update()

    # 次のフレームをスケジュール
    screen.ontimer(animate, 50)


# アニメーションを開始
animate()

screen.mainloop()
