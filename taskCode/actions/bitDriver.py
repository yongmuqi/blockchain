import requests
from selenium import webdriver

post = '54345'


class bitDriver:
    def __init__(self):
        self.driver = None

    # 关闭比特浏览器
    @staticmethod
    def bit_stopBrowser(Id):
        stopUrl = "http://127.0.0.1:" + post + "/browser/close"
        headers = {'id': Id, }
        requests.session().post(stopUrl, json=headers).json()

    # 初始化比特浏览器
    def browser(self, Id, bit_align=None):
        headers = {'id': Id, 'loadExtensions': True}
        openurl = "http://127.0.0.1:" + post + "/browser/open"
        resp = requests.session().post(openurl, json=headers).json()
        chrome_driver = r"D:\\chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", resp['data']['http'])
        self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        # 分割屏幕
        if bit_align:
            # 全屏
            self.driver.maximize_window()
            # 获取屏幕大小
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            if bit_align == 'topLeft':
                self.driver.set_window_rect(0, 0, int(width / 2), int(height / 2))
            elif bit_align == 'topRight':
                self.driver.set_window_rect(int(width / 2), 0, int(width / 2), int(height / 2))
            elif bit_align == 'bottomLeft':
                self.driver.set_window_rect(0, int(height / 2), int(width / 2), int(height / 2))
            elif bit_align == 'bottomRight':
                self.driver.set_window_rect(int(width / 2), int(height / 2), int(width / 2), int(height / 2))
            elif bit_align == 'left':
                self.driver.set_window_rect(0, 0, int(width / 2), height)
            elif bit_align == 'right':
                self.driver.set_window_rect(int(width / 2), 0, int(width / 2), height)
            else:
                pass
        return self.driver
