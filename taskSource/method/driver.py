import time

import requests
from selenium import webdriver


class Driver:
    @staticmethod
    def Driver(adsId, align=None):
        url = 'http://local.adspower.net:50325/api/v1/browser/'
        open_url = url + 'start?user_id=' + adsId + '&open_tabs=1'
        resp = requests.get(open_url).json()
        chrome_driver = resp["data"]["webdriver"]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        driver.set_page_load_timeout(120)
        driver.set_window_size(1280, 800)

        # 分割屏幕
        if align:
            # 全屏
            driver.maximize_window()
            # 获取屏幕大小
            size = driver.get_window_size()
            width = size['width']
            height = size['height']

            if align == 'topLeft':
                driver.set_window_rect(0, 0, int(width / 2), int(height / 2))
            elif align == 'topRight':
                driver.set_window_rect(int(width / 2), 0, int(width / 2), int(height / 2))
            elif align == 'bottomLeft':
                driver.set_window_rect(0, int(height / 2), int(width / 2), int(height / 2))
            elif align == 'bottomRight':
                driver.set_window_rect(int(width / 2), int(height / 2), int(width / 2), int(height / 2))
            elif align == 'left':
                driver.set_window_rect(0, 0, int(width / 2), height)
            elif align == 'right':
                driver.set_window_rect(int(width / 2), 0, int(width / 2), height)
            else:
                pass
        return driver
