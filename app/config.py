from flask import make_response

JSON_MIME_TYPE = 'application/json'


def search_book(books, book_id):
    """
    Gets book by ID.
    :param books: json with all books.
    :param book_id: int
    :return: json for book with given ID
    """
    for book in books:
        if book['ID'] == book_id:
            return book


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE
    return make_response(data, status, headers)
