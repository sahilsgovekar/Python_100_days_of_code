from flask import Flask

app = Flask(__name__)

def bold(fun):
    def wrap():
        return "<b>" + fun() + "<b>"
    return wrap

@app.route("/")
@bold
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)