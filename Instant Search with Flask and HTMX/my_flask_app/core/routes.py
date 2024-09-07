from flask import render_template
from core import app
from core.models import Book

@app.route('/')
def index():
    # Fetch the first 20 books to display by default
    books = Book.query.limit(20).all()
    return render_template("index.html", books=books)
