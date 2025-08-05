from flask import Flask
from flask_restx import Resource, Api, reqparse

# Create the app
app = Flask(__name__)

#Create the api for the app
api = Api(app)

#Global storage
students = []

# Base parser - shared arguments
base_parser = reqparse.RequestParser()
base_parser.add_argument('name', type=str, help='Student name')
base_parser.add_argument('grade', choices=['A', 'B', 'C', 'D', 'E', 'F'], help='Student grade')

## Query student name with wildcard search for their grade for GET in the uri like /students?name=sushil
get_parser = base_parser.copy()

# Parser for POST as JSON Payload {'name': 'xxxx', 'grade': 'yyy'}
#Since we are using the same argument with revised criteria, therefore, we use replace_argument
#Replaces an existing argument with the same name.
#Useful when you’ve copied a parser and want to modify specific argument settings (like required, location, choices, etc.).
#Won’t raise an error if the argument exists — it updates it.

post_parser = base_parser.copy()
post_parser.replace_argument('name', type=str, help='Student name', location='json')
post_parser.replace_argument('grade', choices=['A', 'B', 'C', 'D', 'E', 'F'], help='Student grade', location='json')

#Create the end-point for the api
@api.route("/students")
class Students(Resource):
    @api.expect(get_parser) #Bring the variables under uri serach query
    def get(self):
        args = get_parser.parse_args() #Bring the two variables to use in the following code
        if args.name:
            #Blank filter to search by name(Wildcard search)
            filtered = []
            for search_name in students:
                if args.name.lower() in search_name['name'].lower():
                    filtered.append(search_name)
            return {'students' : filtered}, 200
        elif args.grade:
            #Blank filter to search by grade
            filtered = []
            for search_grade in students:
                if search_grade['grade'] == args.grade:
                    filtered.append(search_grade)
            return {'students': filtered}
        else:
            # Return all students if none of the search crieria meets
            return {'students': students}
    @api.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()
        students.append({
            "name": args.name,
            "grade": args.grade
        })
        return {'message': 'Student added'}, 201
if __name__ == '__main__':
    app.run(debug=True)