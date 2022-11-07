from flask import Flask, render_template
import requests

age_api = "https://api.agify.io/?name="
gender_api = "https://api.genderize.io/?name="


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/<name>")
def predect(name):
    respons = requests.get(url=f"{age_api}{name}")
    age = respons.json()["age"]
    respons = requests.get(url=f"{gender_api}{name}")
    gender = respons.json()["gender"]
    return render_template("predict.html", age=age, gender=gender, name=name)



if __name__ == "__main__":
    app.run(debug=True)