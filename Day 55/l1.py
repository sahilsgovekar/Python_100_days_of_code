from unicodedata import name
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sahil")
def sahil():
    return "<h1>Sahil</h1>"

#takes the variable
@app.route("/<name>")
def greet(name):
    return f"Hey, {name}!! \n whatsup"

if __name__ == "__main__":
    app.run(debug=True)