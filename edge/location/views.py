from location.util import *
from location.models import Device
from django.forms import model_to_dict
import os
import requests
import json


def test(request):
    print(request.GET)
    return success_message()


def register_device(request):
    obj = request.POST

    lng = obj.get('lng')
    lat = obj.get('lat')

    if not (lng and lat):
        return invalid_param_error()

    device = Device.register_device(lng, lat)

    device = model_to_dict(device)

    device.device_id = str(device.device_id)

    return device


def previous_address(request):
    obj = request.GET

    device_id = obj.get('device_id')

    if not device_id:
        return invalid_param_error()

    device = Device.find_device(device_id=device_id)

    if device is None:
        return error_message('Failed')

    device = model_to_dict(device)

    device.device_id = str(device.device_id)

    return success_message(device)


def get_weather(request):

    obj = request.GET

    device_id = obj.get('device_id')

    if device_id == 'default':
        device_id = None

    device = None
    if device_id:
        device = Device.find_device(device_id=device_id)

    api_key = os.environ.get('api_key')
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s' % api_key

    # Payload
    payload = dict()
    payload['considerIp'] = False

    APs = list()
    APs.append({'macAddress': "c0:05:c2:d0:17:69"})
    APs.append({'macAddress': "c0:05:c2:bc:94:5f"})

    payload['wifiAccessPoints'] = APs
    payload = json.dumps(payload)

    # Request
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=payload, headers=headers)

    try:
        r = r.json()

    except ValueError:
        return error_message('Failed to Parse JSON')

    location = r['location']
    accuracy = r['accuracy']

    lat = location['lat']
    lng = location['lng']

    # 6.0km
    if accuracy > 6000 and device is not None:
        lat = device.prev_lat
        lng = device.prev_lng

    if device_id is None:
        device = Device.register_device(lng=lng, lat=lat)

    api_key = os.environ.get('weather_key')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s' % (lat, lng, api_key)

    r = requests.get(url)

    try:
        r = r.json()
        print(r)
    except ValueError:
        return error_message('Failed to Parse JSON')

    weather = r.get('weather', None)
    weather = weather[0]

    return_obj = dict()
    return_obj['weather'] = weather['main']
    return_obj['device_id'] = str(device.device_id)

    return success_message(return_obj)




