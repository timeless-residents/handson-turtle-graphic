import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速


def draw_koch_curve(pen, length, depth):
    """コッホ曲線を描画する関数

    Args:
      pen: Turtleオブジェクト
      length: 線分の長さ
      depth: 再帰の深さ
    """
    if depth == 0:
        pen.forward(length)
    else:
        draw_koch_curve(pen, length / 3, depth - 1)
        pen.left(60)
        draw_koch_curve(pen, length / 3, depth - 1)
        pen.right(120)
        draw_koch_curve(pen, length / 3, depth - 1)
        pen.left(60)
        draw_koch_curve(pen, length / 3, depth - 1)


pen.speed(0)
draw_koch_curve(pen, 200, 3)
turtle.done()
