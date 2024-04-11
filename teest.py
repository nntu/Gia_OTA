from bs4 import BeautifulSoup
import requests
import csv
import json

# Replace checkin/checkout dates if you wish
CHECKIN = "2024-03-30"
CHECKOUT = "2024-03-31"

# Save to CSV file function
def saveToCSV(hotel_info):
    fieldnames = ['URI', 'title', 'price', 'rating', 'quantity']

    # Create csv file, if it's already created, open it
    with open('hotel_data.csv', mode='w', newline='', encoding="utf-8") as csv_file:
        # Convert dictionary into CSV file
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()

        # Write each hotel's information row by row
        for hotel in hotel_info:
            # Converting price to float for formatting
            hotel['price'] = hotel['price']
            writer.writerow(hotel)
            
    print('Data has been saved to hotel_data.csv')

# Save to JSON file function
def saveToJson(hotel_info):
    # Create JSON file, if it had been already created, open it
    with open("hotel_data.json", "w") as json_file:
        # Append info to the JSON file
        json.dump(hotel_info, json_file, indent=4)
    print('Data has been saved to hotel_data.json')

def main():
    # Connecting to the website
    URL = f'https://www.booking.com/searchresults.html?ss=Can+Tho&ssne=Can+Tho&ssne_untouched=Can+Tho&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuALegN6wBsACAdICJDdhNTYwNjQ0LTJjNjMtNGJmYi1hYjRiLWY3ZTU4MGQ3NzRkMtgCBeACAQ&sid=bf3f228a25efbe3ed0fa7286cf307660&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-3709910&dest_type=city&checkin=2024-04-18&checkout=2024-04-19&group_adults=2&no_rooms=1&group_children=0'

    # Change "User-Agent" upon your browser settings
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    # Make a HTTP request GET from the server
    response = requests.get(URL, headers=headers)

    # Empty arrays to store links and hotels in future
    product_links = []
    hotels = []

    # If the request is accessed successfully
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all hotels from the main page and make a list of them
        product_list = soup.find_all('div', class_= 'c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4')

        # Find all links in HTML code of the website "<a href=""></a>"
        for item in product_list:
            for link in item.find_all('a', class_='a78ca197d0'):
                product_links.append(link['href'])

                # Iterate up to 6 links (it could be removed)
                if len(product_links) == 6:
                    break
            if len(product_links) == 6:
                break
    else:
        print(response.status_code)

    # Find and save to the dictionary information about the hotel 
    for link in product_links:
        # HTTP request GET for each link on the main page
        request = requests.get(link, headers=headers)
        soup = BeautifulSoup(request.content, 'html.parser')

        # Find a title of the hotel by HTML tag
        title_el = soup.find('h2', class_='d2fee87262 pp-header__title')
        title = title_el.getText(strip=True) if title_el else print('Title not found')

        # Find a price by HTML tag
        price_el = soup.find('span', class_= 'prco-valign-middle-helper')

        # Convert it to the manageable form 
        price = price_el.getText(strip=True).replace('\xa0zł', '').replace(',', '.') if price_el else print('Price not found')

        # Try to find rating of the hotel by HTML tag
        try:
            rating_el = soup.find('div', class_='ac4a7896c7')
            rating = rating_el.getText(strip=True).replace('Scored ', '') if rating_el else print('Rating not found')
        # If there is no, leave it empty
        except:
            rating = '-'
        
        # Find quantity of the reviews in the hotel's page
        quantity_el = soup.find('span', class_='a3b8729ab1 f45d8e4c32 d935416c47')
        quantity = quantity_el.getText(strip=True).replace('·', '').replace(',', '.').replace(' reviews', '') if quantity_el else 'Quantity of reviews not found'

        # Create a dictionary of the hotel's data
        hotel = {
            'URI': link,
            'title': title,
            'price': price,
            'rating': rating,
            'quantity': quantity
        }

        # Add to the hotels' list
        hotels.append(hotel)

    # Save to CSV, JSON files to operate with data easily
    saveToCSV(hotels)
    saveToJson(hotels)


main()