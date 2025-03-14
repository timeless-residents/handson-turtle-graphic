import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速


def draw_sierpinski(pen, length, depth):
    """シェルピンスキーの三角形を描画する関数

    Args:
      pen: Turtleオブジェクト
      length: 正三角形の一辺の長さ
      depth: 再帰の深さ
    """
    if depth == 0:
        for _ in range(3):
            pen.forward(length)
            pen.left(120)
    else:
        draw_sierpinski(pen, length / 2, depth - 1)
        pen.forward(length / 2)
        draw_sierpinski(pen, length / 2, depth - 1)
        pen.backward(length / 2)
        pen.left(60)
        pen.forward(length / 2)
        pen.right(60)
        draw_sierpinski(pen, length / 2, depth - 1)
        pen.left(60)
        pen.backward(length / 2)
        pen.right(60)


pen.speed(0)
draw_sierpinski(pen, 200, 4)
turtle.done()
