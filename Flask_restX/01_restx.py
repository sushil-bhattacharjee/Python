from flask import Flask
from flask_restx import Api, Resource

# Step 1: Create Flask app
app = Flask(__name__)

# Step 2: Create API instance
api = Api(app)

# Step 3: Create a simple endpoint
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)
    
'''
Explanation:
1. Imports:

Flask - The web framework
Api - Flask-RESTx's main API class
Resource - Base class for creating endpoints

2. Setup:

app = Flask(__name__) - Creates Flask application
api = Api(app) - Creates API instance attached to Flask app

3. Creating an Endpoint:

@api.route('/hello') - Decorator that defines the URL path
class HelloWorld(Resource) - All endpoints must inherit from Resource
def get(self): - Handles GET requests
return {'message': 'Hello, World!'} - Returns JSON automatically

4. Running:

app.run(debug=True) - Starts the server in debug mode

What happens when you run this:

Server starts at http://localhost:5000
You can visit http://localhost:5000/hello and see {"message": "Hello, World!"}
Swagger docs are automatically available at http://localhost:5000/
'''