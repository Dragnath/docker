from flask import Flask
from flask_restful import Resource, Api
import json
import excel_books

app = Flask(__name__)
api = Api(app)

class Books(Resource):
    def get(self):
        books_list = json.loads(excel_books.books_json)
        return books_list


api.add_resource(Books, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
