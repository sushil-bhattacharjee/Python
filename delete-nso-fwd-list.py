import requests

url = "http://10.1.10.39:8080/restconf/data/tailf-ncs:devices/device=CSR1K17031R6/config/tailf-ned-cisco-ios:ip/route/ip-route-forwarding-list=172.30.200.0,255.255.255.0,10.255.255.2"

payload = "{\r\n    \"severity\": \"critical\"\r\n}"
headers = {
  'Accept': 'application/yang-data+xml',
  'Content-Type': 'application/yang-data+xml',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
