#!pip install httpx httpx[http2] selectolax pandas openpyxl (use if required in terminal)

from bs4 import BeautifulSoup
import pandas as pd
import requests
import asyncio
import os
import re
from selectolax.parser import HTMLParser

def clean_text(text):
    """
    Clean the text by removing illegal characters for Excel.
    """
    illegal_chars = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
    return illegal_chars.sub("", text)

def fetch_html(url, headers):
   
    response = requests.get(url, headers=headers)
    
    return response.text if response.status_code == 200 else None


def scrape_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    reviews_data = []
     
    response_text = fetch_html(url, headers)
    soup = BeautifulSoup(response_text, 'lxml') # Parse the HTML as a string
    
    
 
    f = open("demofile2.html", "w",encoding='utf-8')
    f.write(response_text)
    f.close()
    return reviews_data

url = 'https://www.booking.com/hotel/vn/golf-can-tho.vi.html'
da = scrape_reviews(url)
print (da)