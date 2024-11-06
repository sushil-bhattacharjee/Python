import requests
from rich import print as rprint
import urllib3

urllib3.disable_warnings()

url = "http://10.1.10.39:8080/restconf/data/tailf-ncs:devices/device=CSR1K17031R6/config/tailf-ned-cisco-ios:ip/route"

payload = "{\r\n    \"severity\": \"critical\"\r\n}"
headers = {
  'Accept': 'application/yang-data+xml',
  'Content-Type': 'application/yang-data+xml',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

rprint(response.text)
