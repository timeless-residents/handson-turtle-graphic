import tkinter as tk

# 1. メインウィンドウの作成
root = tk.Tk()
root.title("My First GUI")  # ウィンドウのタイトルを設定

# 2. ウィジェットの作成と配置
label = tk.Label(root, text="Hello, Tkinter!")  # ラベルウィジェットを作成
label.pack()  # ラベルをウィンドウに配置

button = tk.Button(root, text="Click Me!")  # ボタンウィジェットを作成
button.pack()  # ボタンをウィンドウに配置

# 3. イベントループの開始
root.mainloop()
