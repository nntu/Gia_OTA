# can tho id: -3709910

import json
import requests

url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

querystring = {"checkout_date":"2024-04-15","order_by":"popularity","filter_by_currency":"VND","room_number":"1","dest_id":"-3709910","dest_type":"city","adults_number":"2","checkin_date":"2024-4-14","locale":"vi","units":"metric","include_adjacency":"true","children_number":"2","categories_filter_ids":"class::4,free_cancellation::1","page_number":"0","children_ages":"5,0"}

headers = {
	"X-RapidAPI-Key": "afb0d2b2e2msh856d559d147eb08p145f1ajsn72b2eaceb7c9",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response_dict = response.json()
print(json.dumps(response_dict, indent=4, sort_keys=True))


with open('thongtin.json', 'w') as f:
    json.dump(response_dict, f)