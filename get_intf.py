import requests
from rich import print as rprint
import urllib3

urllib3.disable_warnings()

url = "https://10.1.10.77:443/restconf/data/Cisco-IOS-XE-native:native/interface"

payload = ""
headers = {
  'Accept': 'application/yang-data+xml',
  'Content-Type': 'application/yang-data+xml',
  'Authorization': 'Basic c3VzaGlsOnN1c2hpbA=='
}

response = requests.get(url=url, headers=headers, verify=False)

rprint(response.text)