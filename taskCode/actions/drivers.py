import time

import requests
from selenium import webdriver

from taskCode.actions.textFile import textFile


class Drivers:
    def __init__(self):
        self.driver = None

    def Driver(self, adsId, align=None):
        url = 'http://local.adspower.net:50325/api/v1/browser/'
        open_url = url + 'start?user_id=' + adsId + '&open_tabs=1'
        resp = requests.get(open_url).json()
        try:
            chrome_driver = resp["data"]["webdriver"]
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
            self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        except:
            textFile.write_txt_data(adsId + "此窗口运行失败，等待5秒再运行")
            time.sleep(5)
            chrome_driver = resp["data"]["webdriver"]
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
            self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        self.driver.set_page_load_timeout(120)

        # 分割屏幕
        if align:
            # 全屏
            self.driver.maximize_window()
            # 获取屏幕大小
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']

            if align == 'topLeft':
                self.driver.set_window_rect(0, 0, int(width / 2), int(height / 2))
            elif align == 'topRight':
                self.driver.set_window_rect(int(width / 2), 0, int(width / 2), int(height / 2))
            elif align == 'bottomLeft':
                self.driver.set_window_rect(0, int(height / 2), int(width / 2), int(height / 2))
            elif align == 'bottomRight':
                self.driver.set_window_rect(int(width / 2), int(height / 2), int(width / 2), int(height / 2))
            elif align == 'left':
                self.driver.set_window_rect(0, 0, int(width / 2), height)
            elif align == 'right':
                self.driver.set_window_rect(int(width / 2), 0, int(width / 2), height)
            else:
                pass
        return self.driver
