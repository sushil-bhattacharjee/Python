from flask import Flask
from flask_restx import Resource, Api, reqparse

# Step 1: Create Flask app
app = Flask(__name__)

# Step 2: Create API instance
api = Api(app)

# Global storage
sales = [] #Stores individual sale

# Parser for sale
sales_parser = reqparse.RequestParser()
sales_parser.add_argument('product', choices=['laptop', 'phone', 'tablet'], required=True)
sales_parser.add_argument('quantity', type=int, required=True)

@api.route('/sales') #Create the API end-point like "http//127.0.0.1:5000/sales"
class Sales(Resource):
    @api.expect(sales_parser) #Enable query parameters for above two variables like /sales?product=xx&quantity=yy
    def post(self):
        args = sales_parser.parse_args() #Make avilable two above variables product and quantity to use in later iteration
        sales.append({
            'product': args.product,
            'quantity': args.quantity
        })
        return {
            'message': 'Sale recorded'
        }, 201

@api.route('/sales/summary')
class SalesSummary(Resource):
    def get(self):
        """Get sales summary - count total quantity per product"""
        # Initialize summary with all prodcuts set to 0
        summary = {
            'laptop': 0,
            'phone': 0,
            'tablet': 0
        }
        
        # Loop through all sales and add quantities
        for sale in sales:
            summary[sale['product']] += sale['quantity']
        return summary
if __name__ == '__main__':
    app.run(debug=True)
    
'''
Step-by-Step Explanation:
1. Initial Setup:
pythonsales = []  # Empty list
summary = {'laptop': 0, 'phone': 0, 'tablet': 0}  # Dictionary with counts
2. Let's say we recorded these sales:
python# After some POST requests, sales list looks like:
sales = [
    {'product': 'laptop', 'quantity': 2},
    {'product': 'phone', 'quantity': 5},
    {'product': 'laptop', 'quantity': 1},
    {'product': 'tablet', 'quantity': 3}
]
3. Now the loop works like this:
First iteration: sale = {'product': 'laptop', 'quantity': 2}

sale['product'] = 'laptop'
sale['quantity'] = 2
summary[sale['product']] = summary['laptop'] = 0 (current value)
summary['laptop'] += 2 → summary['laptop'] becomes 2
Summary now: {'laptop': 2, 'phone': 0, 'tablet': 0}

Second iteration: sale = {'product': 'phone', 'quantity': 5}

sale['product'] = 'phone'
summary['phone'] += 5 → summary['phone'] becomes 5
Summary now: {'laptop': 2, 'phone': 5, 'tablet': 0}

Third iteration: sale = {'product': 'laptop', 'quantity': 1}

sale['product'] = 'laptop'
summary['laptop'] += 1 → summary['laptop'] becomes 2 + 1 = 3
Summary now: {'laptop': 3, 'phone': 5, 'tablet': 0}

Fourth iteration: sale = {'product': 'tablet', 'quantity': 3}

summary['tablet'] += 3 → summary['tablet'] becomes 3
Final summary: {'laptop': 3, 'phone': 5, 'tablet': 3}

The Key Point:
summary[sale['product']] uses the value of sale['product'] as the key to access the summary dictionary.
So if sale['product'] is 'laptop', then summary[sale['product']] is the same as writing summary['laptop'].
'''

