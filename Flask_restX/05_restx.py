from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Parser wth validation and choices
parser_pizza = reqparse.RequestParser()
parser_pizza.add_argument('pizza_type', choices=['margherita', 'pepperoni', 'vegetarian'], required=True)
parser_pizza.add_argument('size', choices=['small', 'medium', 'large'], required=True)
parser_pizza.add_argument('quantity', type=int, required=True)

@api.route("/pizza/order")
class PizzaOrder(Resource):
    @api.expect(parser_pizza) ## This shows parameters in Swagger docs 
                              #(like /calcuate?pizza_type=pepperoni&size=small&quantity=10)
    def post(self):
        args = parser_pizza.parse_args() #Parse arguments gets the values pizza_type, size, quantity
        return {
            "order": f"{args.quantity} {args.size} {args.pizza_type} pizza(s)",
            "status": "Order received"
        }, 201
if __name__ == '__main__':
    app.run(debug=True)