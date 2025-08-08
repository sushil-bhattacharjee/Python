from flask import Flask
from flask_restx import Resource, Api, fields, marshal_with, reqparse

app = Flask(__name__)
api = Api(app)

# Employee model for marshalling
employee_model = api.model("Employee", {
    "username": fields.String(required=True, description="Unique username"),
    "name": fields.String(required=True, description="Full name"),
    "department": fields.String(required=True),
    "salary": fields.Integer(required=True)
})

# In-memory dictionary database
employees_dict = {}

# Parser for POST and PATCH
employee_parser = reqparse.RequestParser()
employee_parser.add_argument("username", type=str, location="json", required=True)
employee_parser.add_argument("name", type=str, location="json", required=True)
employee_parser.add_argument("department", type=str, location="json", required=True)
employee_parser.add_argument("salary", type=int, location="json", required=True)

patch_parser = employee_parser.copy()
patch_parser.replace_argument("username", type=str, location="json", required=False)
patch_parser.replace_argument("name", type=str, location="json", required=False)
patch_parser.replace_argument("department", type=str, location="json", required=False)
patch_parser.replace_argument("salary", type=int, location="json", required=False)

@api.route("/employees")
class EmployeeList(Resource):
    @marshal_with(employee_model)
    def get(self):
        return list(employees_dict.values()), 200

    @api.expect(employee_parser)
    def post(self):
        args = employee_parser.parse_args()
        username = args["username"]
        if username in employees_dict:
            return {"message": f"Employee '{username}' already exists."}, 400
        employees_dict[username] = args
        return {"message": f"Employee '{username}' added."}, 201

@api.route("/employees/<string:username>")
class Employee(Resource):
    @marshal_with(employee_model)
    def get(self, username):
        emp = employees_dict.get(username)
        if emp:
            return emp, 200
        return {"message": "Employee not found."}, 404

    def delete(self, username):
        if username in employees_dict:
            del employees_dict[username]
            return {"message": f"Employee '{username}' deleted."}, 200
        return {"message": "Employee not found."}, 404

    @marshal_with(employee_model)
    @api.expect(patch_parser)
    def patch(self, username):
        emp = employees_dict.get(username)
        if not emp:
            return {"message": "Employee not found."}, 404
        args = patch_parser.parse_args()
        emp.update({k: v for k, v in args.items() if v is not None})
        return emp, 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
