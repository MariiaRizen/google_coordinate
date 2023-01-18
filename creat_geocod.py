import requests


parameters = {'latlng': '40.714224,-73.961452', 'key': ''}
resp = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=parameters)
print(resp)
print(resp.json())

