from flask import Flask
import random

from numpy import number

generated_number = random.randint(0, 10)

app = Flask(__name__)

@app.route("/")
def Home():
    return "<h1>Guess the Number</h1> <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def Guess(number):
    if number > generated_number:
        return "<h1>Too High..!</h1> <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < generated_number:
        return "<h1>Too Low!!</h1> <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1>you Guessed it right</h1> <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)