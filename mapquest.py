import requests

key = "KEY"

requests.get('http://www.mapquestapi.com/geocoding/v1/address', params={'key': key, 'location': 'Denver, CO'})

