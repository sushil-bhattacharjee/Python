from flask import Flask
from flask_restx import Resource, Api, reqparse
import ipaddress

app = Flask(__name__)
api = Api(app)

ip_block_parser = reqparse.RequestParser()
ip_block_parser.add_argument('ip_block', type=str, required=True, help="INPUT IP SUBNET BLOCK like 192.168.8.8/29")
@api.route("/subnetinfo")
class SubnetInfo(Resource):
    @api.expect(ip_block_parser)
    def get(self):
        args = ip_block_parser.parse_args()
        ipblock = args.ip_block
        try:
            net = ipaddress.ip_network(ipblock, strict=False)
            net_add = net.network_address       # 192.168.1.0
            mask = net.netmask               # 255.255.255.0
            broadcast_add = net.broadcast_address     # 192.168.1.255
            total_ip = net.num_addresses         # 256
            prefix_length = net.prefixlen             # 24
            first_usable_ip = list(net.hosts())[0]      # 192.168.1.1 (1st usable IP)
            last_usable_ip = list(net.hosts())[-1]     # 192.168.1.254 (last usable IP)
            usable_ip = len(list(net.hosts()))
            return {
                "Network Address": str(net_add),
                "Broadcast address": str(broadcast_add),
                "Subent mask": str(mask),
                "Prefix length": str(prefix_length),
                "Number of usable hosts": str(usable_ip),
                "First usable host IP": str(first_usable_ip),
                "Last usable host IP": str(last_usable_ip)
            }, 200
        except ValueError:
            return {"error": f"'{ipblock}' is not a valid IP block"}
if __name__ == '__main__':
    app.run(debug=True, port=4999)
        