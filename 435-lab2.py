return_val = {
    "alertData": {
        "countNode": 1,
            "bssids": [
                "aa:bb:cc:dd:ee:ff",
                "11:22:33:44:55:66"
            ],
    "minFirstSeen": 1548512334,
    "maxLastSeen": 1548512802,
    "countIsContained": 0,
    "reason": "Seen on LAN",
    "wiredMac": "aa:bb:cc:dd:ee:f0",
    },
    "alertId": "629378047939282802",
    "alertType": "Air Marshal - Roque AP detected",
    "occuredAt": "2019-01-26T14:18:54.000000Z",
    "organizationId": "123456",
    "organizationName": "Organization",
    "organizationUrl": "https://n1.meraki.com/o/ ... /manage/organization/overview",
    "networkId": "L 123456789012345678",
    "networkName": "Network",
    "networkUrl": "https://n1.meraki.com/ ... /manage/nodes/list",
    "version": "0.1",
    "sharedSecret": "supersecret",  
    "sentAt": "2019-01-26T14:35:20.442869Z",
}


bssids = return_val["alertData"]["bssids"]

for value in bssids:
    print("ALERT: detected a bssid on the network: "+value)