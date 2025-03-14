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
pen.goto(0, 0)
pen.pendown()
pen.speed(0)  # 最速

# 円弧を組み合わせてハートを描画
draw_arc_trigonometry(pen, 50, 225, 45, 90)  # 左側の弧
draw_arc_trigonometry(pen, 50, 135, 315, 90)  # 右側の弧

pen.penup()
pen.goto(-47, -40)  # 弧の端点に移動 (近似値)
pen.pendown()
pen.goto(47, -40)  # もう片方の弧の端点に線で接続 (近似値)

turtle.done()
