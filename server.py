from flask import Flask
import random

random_num = random.randint(0,9)
CORRECT = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3k1NTA2cWVsNDAwMnFoMmp2cDR4NWhiMDd3dmM1bXF1bjBmN2NtMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gHtYDHlV68DTbbZ7JX/giphy.gif"
LOWER = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGIzZGYyNzUwc3pkbjR4cWN1ZndqcXk1MnJwczY5dXZtbHhpajRwbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3q2K5jinAlChoCLS/giphy.gif"
HIGHER = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 align="center"> Guess a number between 0 and 9 </h1>\
        <center><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></center>'

@app.route('/<int:guess>')
def guessnum(guess):
    if guess>random_num:
        return f'<h1 align = "center" style="color: violet"> Too high, try lower 😉</h1>\
            <center><img src={HIGHER}></center>'
    
    if guess<random_num:
        return f'<h1 align = "center" style="color: red"> Too low, try higher 😏</h1>\
            <center><img src={LOWER}></center>'
            
    if guess==random_num:
        return f'<h1 align = "center" style="color: green"> Found me, hehe 😅</h1>\
            <center><img src={CORRECT}></center>'


if __name__ == '__main__':
    app.run(debug=True)