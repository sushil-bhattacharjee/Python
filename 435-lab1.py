return_val = {
    "alertId": "643451796765672516",
    "alertType": "appliances went down",
    "deviceMac": "e0:55:3d:6c:c1: 7a",
    "deviceName": "MX65 c1:7a",
    "deviceSerial": "Q2QN-58EA-XXXX",
    "deviceUrl": "https://n143.meraki.com/Branch-1/n/ ... /manage/nodes/new_wired status",
    "networkId": "L 1234567890",
    "networkName": "Branch 1",
    "networkUrl": "https://n143.meraki.com/Branch-1/n/ ... /manage/nodes/wired_status",
    "occuredAt": "2018-11-10T18:45:20.000000Z",
    "organizationId": "1234567",
    "organizationName": "Meraki Demo",
    "organizationUrl": "https://n143.meraki.com/o/ ... /manage/organization/overview",
    "sentAt": "2018-11-10T18:50:30.479982Z",
    "SharedSecret": "asdf1234",
    "version": "0.1"
}


#Which Python snippet displays the device name and the time at which the switch went down?
print("The Switch: "+return_val['deviceName']+", \
      wentdown at: "+return_val['occuredAt'])