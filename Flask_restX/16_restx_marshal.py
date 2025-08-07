from flask import Flask
from flask_restx import Resource, Api, reqparse, marshal_with, fields

app = Flask(__name__)
api = Api(app)

#Model definition using Flask-RESTX fields
student_inv = api.model("Student",{
    "id": fields.Integer(required=True, description="Unique Student ID"),
    "name": fields.String(required=True, description="Student Name"),
    "grade": fields.String(required=True, description="Grade A/B/C/D/E/F")
})

#Initial Student inventory
students_list = [
    {"id": 1, "name": "Sushil", "grade": "A"},
    {"id": 11, "name": "James Bond", "grade": "B"},
    {"id": 12, "name": "Yug B", "grade": "A"},
    {"id": 13, "name": "Aayu S", "grade": "A"},
    {"id": 14, "name": "Donald Trump", "grade": "F"},
    {"id": 15, "name": "Junior Trump", "grade": "D"},
    {"id": 16, "name": "JD Vence", "grade": "E"}
]

# Parser for the query
query_parser = reqparse.RequestParser()
query_parser.add_argument('id_search', type=int)
query_parser.add_argument('name_search')
query_parser.add_argument('grade_search', choices=['A', 'B', 'C', 'D', 'E', 'F'])

# Parser for the PATCH
patch_parser = reqparse.RequestParser()
patch_parser.add_argument('name_search', location='json')
patch_parser.add_argument('grade_search', choices=['A', 'B', 'C', 'D', 'E', 'F'], location='json')
# Parser for the POST
post_parser = patch_parser.copy()
post_parser.add_argument('id_search', type=int, location='json')


@api.route("/students")
class StudentSearch(Resource):
    @marshal_with(student_inv) # Tells Flask-RESTX to use student_inv model
    @api.expect(query_parser)
    def get(self):
        args = query_parser.parse_args()
        if args.grade_search:
            match_entry = [u for u in students_list if args.grade_search == u["grade"]]
            return match_entry, 200
        else:
            return students_list, 200
#For the post it doesn't require marsha_with since it is appending original list
@api.route("/students/add")
class NewStudent(Resource):
    @api.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()
        students_list.append({
            "id": args.id_search,
            "name": args.name_search,
            "grade": args.grade_search
        })
        return {"message": "new student added"}, 201
#In case if you want to contibue with marsha_with and print the new student details
@api.route("/studend/wMarshalADD")
class NewStudenwMarshal(Resource):
    @marshal_with(student_inv)
    @api.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()
        new_student = {
            "id": args.id_search,
            "name": args.name_search,
            "grade": args.grade_search
        }
        students_list.append(new_student)
        return new_student, 201
@api.route("/students/<int:id>")
class RemoveStudent(Resource):
    def delete(self, id):
        global students_list 
        original_count = len(students_list)
        student_list = [u for u in students_list if u["id"] != id ]
        if len(students_list) < original_count:
            return {"message": f"Student '{id} deleted successfully"}, 200
        else:
            return {"error": f"Student '{id} NOT FOUND"}, 400
        
@api.route("/students/wmarshal/<int:id>")
class RemoveStudentsMarshal(Resource):
    @marshal_with(student_inv)
    def delete(self, id):
        global students_list
        for i, v in enumerate(students_list):
            if v["id"] == id:
                deleted = students_list.pop(i)
                return deleted, 202
        return {"error": f"Student with ID {id} not found."}, 404
    @marshal_with(student_inv)
    @api.expect(patch_parser)
    def patch(self, id):
        args = patch_parser.parse_args()
        for student in students_list:
            if student["id"] == id:
                if args.name_search:
                    student['name'] = args.name_search
                if args.grade_search:
                    student["grade"] = args.grade_search
                return student, 200
        return {"error": f"Student with ID {id} not found"}, 404
if __name__ == '__main__':
    app.run(debug=True, port=4999)
