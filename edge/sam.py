import requests
import os
import json


def main():

    api_key = os.environ.get('api_key', 'AIzaSyDDtY9rLqi1kl2sWJVEz5knD_7lnSCYfNI')
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s' % api_key

    # Payload
    payload = dict()
    payload['considerIp'] = False

    APs = list()
    # for add in mac_address:
    
    APs.append({'macAddress': "c0:05:c2:d0:17:69"})
    APs.append({'macAddress': "c0:05:c2:bc:94:5f"})
    APs.append({'macAddress': "B6:D3:2E:16:4A:54"})
    
    payload['wifiAccessPoints'] = APs
    payload = json.dumps(payload)

    # Request
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=payload, headers=headers)

    try:
        r = r.json()

    except ValueError:
        return error_message('Failed to Parse JSON')
    print(r)
    location = r['location']
    accuracy = r['accuracy']

if __name__=='__main__':
    # main()

    r = requests.get('https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=c0:05:c2:bc:94:5f')
    print(r.text)