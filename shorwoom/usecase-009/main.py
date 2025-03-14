import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速


def draw_circle_trigonometry(pen, radius, steps):
    """三角関数を用いて円を描画する関数

    Args:
      pen: Turtleオブジェクト
      radius: 半径
      steps: 円を近似する線の数
    """
    for i in range(steps):
        angle = 2 * math.pi * i / steps
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pen.goto(x, y)  # 原点からの相対座標
    pen.goto(radius, 0)  # 最初の点に戻る


pen.penup()
pen.goto(0, -50)  # 円の中心を原点にするため、少し下に移動
pen.pendown()
draw_circle_trigonometry(pen, 50, 360)  # 半径50、360ステップで円を描画
turtle.done()
