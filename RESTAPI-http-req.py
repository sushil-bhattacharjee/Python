import requests

#To avoid warnings
requests.packages.urllib3.disable_warnings()

#represent the yang data in json
headers = {"Accept": "application/yang-data+json"}

device = {
    "host": "10.1.10.29",
    "port": "443",
    "user": "sushil",
    "password": "sushil"
}

url = f"https://{device['host']}:{device['port']}/restconf/data/ietf-interfaces:interfaces"
    
response = requests.get(url=url, headers=headers, auth=(device["user"], device["password"]), verify=False)    

print(f"HTTP REST API Status Code, \n", response)
print()
print(f"Check the entire get response,\n", response.text)

