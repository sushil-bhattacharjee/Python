from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


# Global storage - like a simple database
orders = [] # This stores all orders

# Parse for creating orders
order_parser = reqparse.RequestParser()
order_parser.add_argument('item', required=True, help='What item?')
order_parser.add_argument('quantity', type=int, required=True, help='How many?')

@api.route('/orders')
class Orderlist(Resource):
    @api.expect(order_parser)
    def post(self):
        """Create a new order"""
        args = order_parser.parse_args()
        # Add to Global storage
        orders.append({
            'item': args.item,
            'quantity': args.quantity
        })
        return {
            'message': 'Order added',
            'total_orders': len(orders)
        }, 201
        
    def get(self):
        """Get all orders"""
        return {
            'orders': orders,
            'total': len(orders)
        }
if __name__ == '__main__':
    app.run(debug=True)