from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
 



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
    
     
   
    
    print(simpleTable)
    # to get the row count len method
 
    # to close the browser
    driver.quit ()

if __name__ == '__main__':
      
    url = 'https://www.booking.com/hotel/vn/muong-thanh-can-tho.html'
    
    GetData(url)
