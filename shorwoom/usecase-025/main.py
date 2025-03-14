import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

particles = []

# パーティクルを作成
for _ in range(50):
    p = turtle.Turtle()
    p.shape("circle")
    p.shapesize(0.2)
    p.color(random.random(), random.random(), random.random())
    p.penup()
    p.goto(0, 0)
    p.speed(0)

    # ランダムな方向と速度
    angle = random.uniform(0, 360)
    p.setheading(angle)
    p.speed = random.uniform(1, 5)
    p.life = 100  # パーティクルの寿命

    particles.append(p)


def animate():
    for p in particles:
        p.forward(p.speed)
        p.life -= 1

        # 寿命が尽きたらリセット
        if p.life <= 0:
            p.goto(0, 0)
            angle = random.uniform(0, 360)
            p.setheading(angle)
            p.speed = random.uniform(1, 5)
            p.life = 100

    screen.update()
    screen.ontimer(animate, 20)


animate()

screen.mainloop()
