from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route("/greet/<name>")
class Greetings(Resource):
    def get(self, name):
        return {"greeting": f"Hello, {name}!"}
    
if __name__ == '__main__':
    app.run(debug=True)