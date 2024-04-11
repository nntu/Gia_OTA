from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
 

import pandas as pd

def initDriver():
    path = os.getcwd()
    dirdriver = path + "/" + "drivers/chromedriver.exe"
    CHROMEDRIVER_PATH = dirdriver
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControllered")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option('useAutomationExtension', False)
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        
        "download_restrictions": 0,  'safebrowsing.enabled': False,
                     'safebrowsing.disable_download_protection': True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--start-maximized")  # open Browser in maximized mode
#     # overcome limited resource problems
#     chrome_options.add_argument("--disable-dev-shm-usage")
#    # chrome_options.add_argument("--headless=new")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(service=Service(executable_path=dirdriver), options=chrome_options )
    #driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    # params = {'cmd': 'Page.setDownloadBehavior',
    #               'params': {'behavior': 'allow', 'downloadPath': os.getcwd()}}
    # driver.execute("send_command", params)
    driver.implicitly_wait(10)
    return driver



def GetData(url ):
    
   
    driver = initDriver()
    driver.get(url)
    driver.implicitly_wait(20)
    simpleTable = driver.find_element(By.XPATH , '//*[@id="hprt-table"]')
    file = open("output.html", "w",encoding='utf-8')
    file.write(simpleTable.get_attribute("outerHTML"))
    file.close()
    
    df1 = pd.read_html(simpleTable.get_attribute("outerHTML"))[0]
    print(df1)
    df1.to_excel("muonghanh.xlsx")
    
    print(simpleTable)
    # to get the row count len method
 
    # to close the browser
    #driver.quit ()

if __name__ == '__main__':
      
    url = 'https://www.booking.com/hotel/vn/golf-can-tho.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=55062823_0_2_1_0;checkin=2024-04-12;checkout=2024-04-13;dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=9;highlighted_blocks=55062823_0_2_1_0;hpos=9;matching_block_id=55062823_0_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=55062823_0_2_1_0__160200294;srepoch=1712841056;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'
    
    GetData(url)
