import httpx
from rich import print as rprint

headers = {"Accept": "application/yang-data+json"}
my_url = "https://10.1.10.29/restconf/data/ietf-interfaces:interfaces"
def pull_info(url):
    with httpx.Client(verify=False) as Client:
        response = Client.get(url, headers=headers, auth=("sushil", "sushil"))
        return response.text
    
results = pull_info(my_url)
rprint(results)
