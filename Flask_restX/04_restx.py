from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


# Step 1: Create a Parser
parser = reqparse.RequestParser() #RequestParser lets you handle query parameters (like ?age=25&city=Sydney)
parser.add_argument('num1', type=int)
parser.add_argument('num2', type=int)
@api.route("/calculate")
class Calculator(Resource):
    @api.expect(parser) ## This shows parameters in Swagger docs (like /calcuate?num1=7&num2=8)
    def get(self):
        args = parser.parse_args() #Parse arguments gets the values num1 and num2
        output = args.num1 + args.num2 #Access values: args['age'] or args.age
        # return output, 200
        return {
            'result': output,
            'calculation': f"{args.num1} + {args.num2} = {output}"
        }
    
if __name__ == '__main__':
    app.run(debug=True)
    
