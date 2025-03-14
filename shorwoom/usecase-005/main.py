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


# 例：正五角形を描画
draw_polygon(pen, 5, 100)
turtle.done()  # 描画を完了し、ウィンドウを維持
