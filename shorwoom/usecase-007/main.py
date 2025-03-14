import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速


def draw_polygon(pen, sides, length):
    """正多角形を描画する関数

    Args:
      pen: Turtleオブジェクト
      sides: 辺の数
      length: 辺の長さ
    """
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.right(angle)


def draw_star(pen, points, length, skip):
    """星形を描画する関数

    Args:
      pen: Turtleオブジェクト
      points: 頂点の数
      length: 辺の長さ（外側の円の半径）
      skip: スキップする頂点の数
    """
    angle = 360 / points
    for _ in range(points):
        pen.forward(length)
        pen.right(angle * skip)


# 例：五芒星を描画
pen.fillcolor("yellow")
pen.begin_fill()
draw_polygon(pen, 5, 100)
pen.end_fill()

pen.penup()
pen.goto(150, 0)  # 少し右に移動
pen.pendown()

pen.color("blue")
draw_star(pen, 7, 100, 3)  # 七芒星を描画
turtle.done()
