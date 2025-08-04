from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Step 1: Create a parser
parser = reqparse.RequestParser()
parser.add_argument('age', type=int, help='Your age')
parser.add_argument('city', type=str, help='Your city')

@api.route('/person')
class Person(Resource):
    @api.expect(parser)  # This shows parameters in Swagger docs
    def get(self):
        # Step 2: Parse the arguments
        args = parser.parse_args()
        return {
            'age': args['age'],
            'city': args['city'],
            'message': f'You are {args["age"]} years old from {args["city"]}'
        }

if __name__ == '__main__':
    app.run(debug=True)