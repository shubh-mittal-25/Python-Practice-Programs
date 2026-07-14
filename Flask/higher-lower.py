from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

num = randint(0,9)

@app.route("/<int:guess>")
def check(guess):
    if guess < num:
        return ('<h1>f"Your guess is low!"<h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif guess > num:
        return ('<h1>f"Your guess is high!"<h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1>f"You are correct!"<h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)