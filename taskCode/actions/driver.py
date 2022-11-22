import requests
from selenium import webdriver


class Driver:
    @staticmethod
    def Driver(open_url):
        resp = requests.get(open_url).json()
        chrome_driver = resp["data"]["webdriver"]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        driver.maximize_window()
        driver.set_page_load_timeout(120)
        return driver
