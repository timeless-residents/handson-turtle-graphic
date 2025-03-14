import turtle
import time

# 画面の設定
screen = turtle.Screen()
screen.title("カスタムタートル画像のデモ")
screen.bgcolor("lightblue")

# 画像ファイルへの絶対パスを指定（GIF形式を使用）
turtle_image = (
    "/Users/studio/work/github/handson-turtle-graphic/shorwoom/usecase-017/turtle.gif"
)

# GIF画像をタートルの形状として登録
screen.register_shape(turtle_image)

# タートルを作成
t = turtle.Turtle()
t.shape(turtle_image)  # タートルの形状を登録した画像に変更
t.pensize(3)
t.speed(1)  # ゆっくり動かす

# タートルを動かす
t.penup()
t.goto(-150, 0)
t.pendown()

# 四角形を描く
for _ in range(4):
    t.forward(100)
    t.right(90)
    time.sleep(0.5)  # 動きを見やすくするために少し待つ

# 別の場所に移動
t.penup()
t.goto(50, 0)
t.pendown()

# 星を描く
t.color("red")
for _ in range(5):
    t.forward(100)
    t.right(144)
    time.sleep(0.5)

# 完了メッセージ
t.penup()
t.goto(0, -150)
t.color("black")
t.write("カスタム画像の使用成功!", align="center", font=("Arial", 16, "bold"))

# 画面を表示したまま維持
turtle.done()
