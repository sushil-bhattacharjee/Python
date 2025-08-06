from flask import Flask
from flask_restx import Resource, Api, reqparse
import ipaddress

app = Flask(__name__)
api = Api(app)

ip_address_parser = reqparse.RequestParser()
ip_address_parser.add_argument('ip')
@api.route("/ipinfo")
class IPinfo(Resource):
    @api.expect(ip_address_parser)
    def get(self):
        args = ip_address_parser.parse_args()
        ip = args.ip 
        try: 
            addr = ipaddress.ip_address(ip)
            private = addr.is_private
            loopback = addr.is_loopback
            reserved = addr.is_reserved
            multicast = addr.is_multicast
            global_add = addr.is_global
            return {
                    "ip": ip,
                    "is_private": private,
                    "is_loopback": loopback,
                    "is_multicast": multicast,
                    "is_reserved": reserved,
                    "is_global": global_add
                    }, 200
        except ValueError:
            return {"error": f"'{ip}' is not a valid IP address"}, 400
if __name__ == '__main__':
    app.run(debug=True, port=4999)
