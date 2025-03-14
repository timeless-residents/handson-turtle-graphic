import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速

import time


def draw_koch_curve_colored(pen, length, depth):
    """コッホ曲線を描画し、深さに応じて色を変える関数

    Args:
      pen: Turtleオブジェクト
      length: 線分の長さ
      depth: 再帰の深さ
    """
    if depth == 0:
        pen.forward(length)
    else:
        color = (depth / 5, 1 - (depth / 5), 0)  # 深さに応じて色を変化させる (RGB)
        pen.color(color)
        draw_koch_curve_colored(pen, length / 3, depth - 1)
        pen.left(60)
        draw_koch_curve_colored(pen, length / 3, depth - 1)
        pen.right(120)
        draw_koch_curve_colored(pen, length / 3, depth - 1)
        pen.left(60)
        draw_koch_curve_colored(pen, length / 3, depth - 1)


pen.speed(0)
turtle.colormode(1.0)  # カラーモードを1.0に設定 (RGBの範囲を0.0〜1.0にする)

start_time = time.time()
draw_koch_curve_colored(pen, 200, 5)
end_time = time.time()

print(f"実行時間: {end_time - start_time:.4f}秒")
turtle.done()
