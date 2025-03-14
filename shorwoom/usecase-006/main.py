import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速


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
draw_star(pen, 5, 100, 2)
turtle.done()  # 描画を完了し、ウィンドウを維持
