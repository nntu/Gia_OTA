import requests

url = "https://booking-com.p.rapidapi.com/v2/hotels/search-by-coordinates"

querystring = {"checkin_date":"2024-04-14","room_number":"1","checkout_date":"2024-04-15","latitude":"10.0438775","adults_number":"2","units":"metric","filter_by_currency":"VND","order_by":"popularity","locale":"vi","longitude":"105.7908973","page_number":"0","children_number":"2","include_adjacency":"true","children_ages":"5,0","categories_filter_ids":"class::2,class::4,free_cancellation::1"}

headers = {
	"X-RapidAPI-Key": "afb0d2b2e2msh856d559d147eb08p145f1ajsn72b2eaceb7c9",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())