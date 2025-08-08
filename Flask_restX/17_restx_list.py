# ✅ Case-1: Books API using List (with @marshal_with and list comprehension)
from flask import Flask
from flask_restx import Resource, Api, fields, reqparse, marshal_with

app = Flask(__name__)
api = Api(app)

# Book model definition
book_model = api.model("Book", {
    "title": fields.String(required=True, description="Book Title"),
    "author": fields.String(required=True, description="Author Name"),
    "rating": fields.String(required=True, description="Rating out of 5")
})

# Start with an empty list
books_list = []

# Parser for GET/POST/PATCH
book_parser = reqparse.RequestParser()
book_parser.add_argument("title", type=str, location='json')
book_parser.add_argument("author", type=str, location='json')
book_parser.add_argument("rating", type=str, location='json')

@api.route("/books")
class Books(Resource):
    @marshal_with(book_model)
    def get(self):
        return books_list, 200

    @marshal_with(book_model)
    @api.expect(book_parser)
    def post(self):
        args = book_parser.parse_args()
        # Check for duplicates
        if any(b["title"] == args.title for b in books_list):
            api.abort(409, f"Book with title '{args.title}' already exists")
        new_book = {"title": args.title, "author": args.author, "rating": args.rating}
        books_list.append(new_book)
        return new_book, 201

@api.route("/books/<string:title>")
class BookByTitle(Resource):
    @marshal_with(book_model)
    @api.expect(book_parser)
    def patch(self, title):
        args = book_parser.parse_args()
        for book in books_list:
            if book["title"] == title:
                if args.author:
                    book["author"] = args.author
                if args.rating:
                    book["rating"] = args.rating
                return book, 200
        return {"error": f"Book with title '{title}' not found"}, 404

    def delete(self, title):
        global books_list
        original_count = len(books_list)
        books_list = [b for b in books_list if b["title"] != title]
        if len(books_list) < original_count:
            return {"message": f"Book '{title}' deleted successfully"}, 200
        return {"error": f"Book '{title}' not found"}, 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
