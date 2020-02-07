import requests

response = requests.get('https://randomuser.me/api')

print('Your random username is {0}'.format(response.json()['results'][0]['login']['username']))