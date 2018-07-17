from flask import Flask,make_response
from helper import is_isbn_or_key

app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q,page):
    is_isbn_or_key(q)


if __name__ == '__main__':
    app.run()