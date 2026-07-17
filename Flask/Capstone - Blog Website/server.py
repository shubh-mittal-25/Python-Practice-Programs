from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HOMEPAGE</h1>"

@app.route("/guess/<string:name>")
def guess(name):
    gender_response = requests.get("https://api.genderize.io", params={'name': name})
    gender_response = gender_response.json()
    gender = gender_response["gender"]

    age_response = requests.get("https://api.agify.io", params={'name': name})
    age_response = age_response.json()
    age = age_response["age"]

    return render_template("index.html",name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
