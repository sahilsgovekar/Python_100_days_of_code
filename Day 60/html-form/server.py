from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    username = request.form["name"]
    passward = request.form["pass"]
    return render_template("login.html", username=username, passward=passward)
    



if __name__ == "__main__":
    app.run(debug=True)