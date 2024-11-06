USERNAME = '<USERNAME>' # Example USERNAME = 'devnetuser'
PASSWORD = '<PASSWORD' # Example PASSWORD = 'Cisco123!'

# URLS
DEVICES_URL  = '/dna/intent/api/v1/network-device'

def get_dnac_jwt_token():
    response = requests.post(BASE_URL + AUTH_URL,
                             auth=HTTPBasicAuth(USERNAME, PASSWORD),
                             verify=False)

    token = response.json()['Token']
    return token

payload= {
    'destIP': dst_ip_address,
    'inclusions': [
        'INTERFACE-STATS',
        'ACL-TRACE',
        'DEVICE-STATS'
    ],
    'protocol': 'icmp'
    }
