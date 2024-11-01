import requests

api_key = "API KEY HERE"
url = 'https://the-one-api.dev/v2/character'
authorization_headers = {
	'Authorization: Bearer ' + api_key
}
response = requests.get(url, headers=authorization_headers)
print(response.status_code)

import apikey

apikey.save("THE_ONE_API_KEY", "YOUR_API_KEY_HERE")

the_one_api_key = apikey.load("THE_ONE_API_KEY")