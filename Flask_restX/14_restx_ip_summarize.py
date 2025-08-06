import ipaddress
from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

network_parser = reqparse.RequestParser()
network_parser.add_argument('subnet1', required=True, type=str)
network_parser.add_argument('subnet2', required=True, type=str)

@api.route("/CIDRsummary")
class CIDRsummary(Resource):
    @api.expect(network_parser)
    def get(self):
        args = network_parser.parse_args()
        ip_block1 = args.subnet1
        ip_block2 = args.subnet2
        try: 
            networks = [ipaddress.ip_network(ip_block1), ipaddress.ip_network(ip_block2)]
            result = ipaddress.collapse_addresses(networks)
            cidr = [str(net) for net in result]
            return {"CIDR summary": str(cidr)}, 200
        except ValueError:
            return {"error": f"'{ip_block1}' andor '{ip_block2}' are not valid"}, 400
if __name__ == '__main__':
    app.run(debug=True, port=4999)