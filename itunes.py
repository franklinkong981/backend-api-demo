import requests

res = requests.get('https://itunes.apple.com/search', params={'terms': 'Jack Johnson', 'limit': 5})

data = res.json()
for result in data['results']:
    print(result['trackName'])
    print(result['collectionName'])