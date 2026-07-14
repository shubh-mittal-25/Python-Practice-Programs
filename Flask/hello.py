from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align:center">Hello, World!</h1>'
            '<p>Hello, World!</p>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWhldWlyNzRiNmplYWoyY2F5anlqcTY2ZzNzM3ZqMWduODl0NnV3aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W1T9kHIsG9nbTU1P6y/giphy.gif">')


@app.route("/bye")
def say_bye():
    return "Bye, World!"

@app.route("/username/<name>/<int:age>")
def greet(name,age):
    return f"Hello, {name}! Your age is {age} years old!"



if __name__ == "__main__":
    app.run(debug=True)