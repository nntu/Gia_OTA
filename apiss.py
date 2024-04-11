import requests
import json
url = "https://booking-com.p.rapidapi.com/v2/hotels/details"

querystring = {"currency":"VND","locale":"vi","checkout_date":"2024-04-17","hotel_id":"2349834","checkin_date":"2024-04-16"}

headers = {
	"X-RapidAPI-Key": "afb0d2b2e2msh856d559d147eb08p145f1ajsn72b2eaceb7c9",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_dict = response.json()
with open('data.json', 'w') as f:
    json.dump(response_dict, f)
print(json.dumps(response_dict, indent=4, sort_keys=True))