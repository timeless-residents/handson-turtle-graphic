import turtle
import random

# スクリーンの設定
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("スライディングパズル")
screen.tracer(0)

# パズルの設定
grid_size = 3  # 3x3のパズル
tile_size = 100

# パズルの状態
board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0は空白を表す
blank_row, blank_col = 2, 2  # 空白の位置

# タイルを描画するためのタートル
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)


# クリック処理
def handle_click(x, y):
    global blank_row, blank_col

    # クリックされたタイルの位置を計算
    grid_x = int((x + 150) // tile_size)
    grid_y = int((150 - y) // tile_size)

    # 範囲外のクリックは無視
    if not (0 <= grid_x < grid_size and 0 <= grid_y < grid_size):
        return

    # 空白と隣接しているか確認
    if (abs(grid_y - blank_row) == 1 and grid_x == blank_col) or (
        abs(grid_x - blank_col) == 1 and grid_y == blank_row
    ):
        # タイルを移動
        board[blank_row][blank_col] = board[grid_y][grid_x]
        board[grid_y][grid_x] = 0
        blank_row, blank_col = grid_y, grid_x
        draw_board()

        # クリア判定
        if check_win():
            pen.goto(0, 0)
            pen.write("クリア！", align="center", font=("Arial", 24, "normal"))


# 勝利判定
def check_win():
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal


# パズルの描画
def draw_board():
    pen.clear()
    for i in range(grid_size):
        for j in range(grid_size):
            x = j * tile_size - 150 + tile_size // 2
            y = 150 - i * tile_size - tile_size // 2

            if board[i][j] != 0:  # 空白以外のタイルを描画
                pen.goto(x, y)
                pen.pendown()
                pen.fillcolor("lightblue")
                pen.begin_fill()
                for _ in range(4):
                    pen.forward(tile_size - 10)
                    pen.left(90)
                pen.end_fill()
                pen.penup()

                # タイルの数字を描画
                pen.goto(x, y - 10)
                pen.write(str(board[i][j]), align="center", font=("Arial", 20, "bold"))


# パズルをシャッフル
def shuffle_puzzle(moves=100):
    global blank_row, blank_col

    for _ in range(moves):
        # 可能な移動方向をリスト化
        possible_moves = []
        if blank_row > 0:
            possible_moves.append((-1, 0))  # 上
        if blank_row < grid_size - 1:
            possible_moves.append((1, 0))  # 下
        if blank_col > 0:
            possible_moves.append((0, -1))  # 左
        if blank_col < grid_size - 1:
            possible_moves.append((0, 1))  # 右

        # ランダムに移動方向を選択
        dr, dc = random.choice(possible_moves)
        new_row, new_col = blank_row + dr, blank_col + dc

        # タイルを移動
        board[blank_row][blank_col] = board[new_row][new_col]
        board[new_row][new_col] = 0
        blank_row, blank_col = new_row, new_col

    draw_board()


# 初期描画とイベント設定
draw_board()
shuffle_puzzle()
screen.onclick(handle_click)

screen.mainloop()
