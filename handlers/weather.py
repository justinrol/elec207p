import requests
import json


def main():
	api_key = 'AIzaSyDDtY9rLqi1kl2sWJVEz5knD_7lnSCYfNI'
	url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s' % api_key

	payload = dict()
	payload['considerIp'] = 'false'

	APs = list()
	APs.append({'macAddress': 'c0:5:c2:d0:17:70'})
	APs.append({'macAddress': 'e4:3e:d7:3c:c5:92'})
	APs.append({'macAddress': 'c0:05:c2:bc:94:59'})

	payload['wifiAccessPoints'] = APs
	payload = json.dumps(payload)
	
	# Request Deatilas
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

	r =  requests.post(url, data=payload, headers=headers)

	return r.json()

if __name__=='__main__':
	print(main())

# curl -d @sample.json -H "Content-Type: application/json" -i "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDDtY9rLqi1kl2sWJVEz5knD_7lnSCYfNI"