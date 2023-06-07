from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Browse:
    
    def __init__(self, symbol):
        self.symbol = symbol
        pass

    def get_price(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        
        serv_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=serv_obj,options=options)
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        
        search_box.send_keys(self.symbol)
        search_box.submit()
        
        price = driver.find_element(By.CSS_SELECTOR, ".NprOob").text
        return price
