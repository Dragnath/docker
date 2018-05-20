from flask import (Flask, render_template,
                   Response, abort, jsonify, request)
from config import JSON_MIME_TYPE, search_book
import json
import excel_books as eb

app = Flask(__name__)
books_list = json.loads(eb.books_json)


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/book')
def book_list():
    response = Response(
        json.dumps(books_list), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = search_book(books_list, book_id)
    if book is None:
        abort(404)
    content = json.dumps(book)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.route("/user", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
