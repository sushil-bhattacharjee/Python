from flask import Flask
from flask_restx import Resource, Api, reqparse

#Create the app using Flask
app = Flask(__name__)

#Create the api using Api
api = Api(app)

movies_list = []

#Create base parser for movies name, genre 
base_parser = reqparse.RequestParser()
base_parser.add_argument('title', type=str, help="Movie name")
base_parser.add_argument('genre', type=str, choices=['action', 'thriller', 'drama', 'sci-fi'], help='Movie type')

get_parser = base_parser.copy()

post_parser = base_parser.copy()
post_parser.replace_argument('title', required=True, location='json')
post_parser.replace_argument('genre', required=True, location='json', choices=['action', 'thriller', 'drama', 'sci-fi'])

@api.route('/movies')
class MovieName(Resource):
    @api.expect(get_parser)
    def get(self):
        args = get_parser.parse_args()
        
        if args.title:
            filtered_movie = []
            for movie_name in movies_list:
                if args.title.lower() in movie_name['title'].lower():
                    filtered_movie.append(movie_name)
            return filtered_movie, 200
        elif args.genre:
            filtered_movie = []
            for movie_genre in movies_list:
                if movie_genre['genre'] == args.genre:
                    filtered_movie.append(movie_genre)
            return filtered_movie, 200
        else:
            movies_list, 200
    
    @api.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()
        movies_list.append({
            "title": args.title,
            "genre": args.genre
        })
        return {'message': 'Movie name added'}, 201
    
if __name__ == '__main__':
    app.run(debug=True)