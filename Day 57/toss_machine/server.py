from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    yr = date.today().year
    t = random.randint(1, 2)
    if t == 1:
        toss = "head"
    else:
        toss = "tail"
    return render_template("index.html", toss=toss, year=yr)


if __name__ == "__main__":
    app.run(debug=True)