import requests

url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

querystring = {"name":"Can Tho","locale":"vi"}

headers = {
	"X-RapidAPI-Key": "afb0d2b2e2msh856d559d147eb08p145f1ajsn72b2eaceb7c9",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())