from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


# Global storage
books = []

book_parser = reqparse.RequestParser()
book_parser.add_argument('title', required=True)
book_parser.add_argument('author', required=True)
book_parser.add_argument('genre', required=True, choices=['fiction', 'non-fiction', 'mystery', 'romance'])
@api.route("/books")
class BookLibrary(Resource):
    @api.expect(book_parser) #Bring the variables under query parameters like ?title=xx&author=yy&genre=zz
    def post(self): #"""Create a new order"""
        args = book_parser.parse_args() #Bring the three varaibles to ammend the order
        books.append({
            'title': args.title,
            'author': args.author,
            'genre': args.genre
        })
        return {
            "message": "book added",
            "total_books": len(books)
        }, 201
        
    def get(self):
        return {
            "books": books,
            'total': len(books)
        }, 200
@api.route("/books/summary")
class BookSummary(Resource):
    def get(self):
        summary = {
            "fiction": 0,
            "non-fiction": 0,
            "mystery": 0,
            "romance": 0
        }
        for book in books:
            summary[book['genre']] += 1
        return summary, 200
if __name__ == '__main__':
    app.run(debug=True)