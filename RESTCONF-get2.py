import requests
from rich import print as rprint
import urllib3

urllib3.disable_warnings()

headers = {"Accept": "application/yang-data+json"}
#url = "https://10.1.10.29/restconf/data/native/router/Cisco-IOS-XE-bgp:bgp"
#urlopenconfig = "https://10.1.10.29/restconf/data/native?content=config"
urlopenconfig = "https://10.1.10.29/restconf/data/native/ntp?content=config"

#response = requests.get(url=url, headers=headers, auth=("sushil","sushil"), verify=False)
#rprint(response.text)
response1 = requests.get(url=urlopenconfig, headers=headers, auth=("sushil","sushil"), verify=False)
rprint(response1.text)