import turtle
import requests
import json

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Web APIから取得したデータによる棒グラフ")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_bar(height, label, color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(90)
    pen.forward(height)
    pen.write(label, align="center")
    pen.right(90)
    pen.forward(40)
    pen.right(90)
    pen.forward(height)
    pen.left(90)
    pen.end_fill()


def get_user_post_counts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = json.loads(response.text)
        user_post_counts = {}
        for post in posts:
            user_id = post["userId"]
            if user_id in user_post_counts:
                user_post_counts[user_id] += 1
            else:
                user_post_counts[user_id] = 1
        return user_post_counts
    else:
        print("APIリクエストに失敗しました:", response.status_code)
        return None


user_post_counts = get_user_post_counts()

if user_post_counts:
    x_start = -150
    pen.penup()
    pen.goto(x_start, -100)
    pen.pendown()

    colors = [
        "red",
        "green",
        "blue",
        "orange",
        "purple",
        "pink",
        "brown",
        "gray",
        "cyan",
        "magenta",
    ]
    i = 0
    for user_id, post_count in user_post_counts.items():
        color = colors[i % len(colors)]
        draw_bar(post_count * 10, f"User {user_id}", color)  # データの値を調整
        i += 1

screen.mainloop()
