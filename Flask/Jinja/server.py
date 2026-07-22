from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("examples.html")

@app.route("/guess/<string:name>")
def guess(name):
    gender_response = requests.get("https://api.genderize.io", params={'name': name})
    gender_response = gender_response.json()
    gender = gender_response["gender"]

    age_response = requests.get("https://api.agify.io", params={'name': name})
    age_response = age_response.json()
    age = age_response["age"]

    return render_template("guess.html",name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("multiline.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
