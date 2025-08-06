from flask import Flask
from flask_restx import Resource, Api, reqparse
import ipaddress
import subprocess
import platform

app = Flask(__name__)
api = Api(app)

ip_add_validator_parser = reqparse.RequestParser()
ip_add_validator_parser.add_argument('ip', type=str, help="validate IP address", required=True)

ping_parser = ip_add_validator_parser.copy()
ping_parser.add_argument("count", type=int, default=4, help="count the number of times to ping", required=True)
@api.route("/validate")
class IPaddressValidator(Resource):
    @api.expect(ip_add_validator_parser)
    def get(self):
        args = ip_add_validator_parser.parse_args()
        try:
            ipaddress.ip_address(args.ip)
            return {"valid": True}
        except ValueError:
            return {"valid": False}
@api.route("/ping")
class IPrechhability(Resource):
    @api.expect(ping_parser)
    def get(self):
        args = ping_parser.parse_args()
        ip = args.ip 
        count = args.count 
        try:
            ping_count_flag = "-n" if platform.system() == "windows" else "-c"
            result = subprocess.run(["ping", ping_count_flag, str(count), ip], capture_output=True, text=True)
            return {"output": result.stdout}, 200
        except Exception as e:
            return {"error": str(e)}, 500
if __name__ == '__main__':
    app.run(debug=True, port=4999)