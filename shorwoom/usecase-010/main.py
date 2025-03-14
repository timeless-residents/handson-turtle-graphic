import turtle
import math

# タートルの設定
pen = turtle.Turtle()
pen.speed(0)  # 最速


def draw_arc_trigonometry(pen, radius, start_angle, end_angle, steps):
    """三角関数を用いて弧を描画する関数

    Args:
      pen: Turtleオブジェクト
      radius: 半径
      start_angle: 開始角度（度数法）
      end_angle: 終了角度（度数法）
      steps: 弧を近似する線の数
    """
    angle_range = end_angle - start_angle
    for i in range(steps):
        angle = math.radians(
            start_angle + angle_range * i / steps
        )  # 度数法からラジアンに変換
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pen.goto(x, y)


pen.penup()
pen.goto(0, 0)  # 原点に移動
pen.pendown()
pen.setheading(0)  # タートルの向きを右向きに設定
draw_arc_trigonometry(pen, 50, 0, 180, 180)  # 半径50、0度から180度の弧を描画
turtle.done()
