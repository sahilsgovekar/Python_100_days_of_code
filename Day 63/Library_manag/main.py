from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

# all_books = []

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(250), unique=True, primary_key=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html",len = len(all_books) ,books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        bname = request.form["bname"]
        bauthor = request.form["bauthor"]
        brating = request.form["brating"]
        # c_book = {
        #     "title" : bname,
        #     "author" : bauthor,
        #     "rating" : brating
        # }

        new_book = Book(title=bname, author=bauthor, rating=brating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

