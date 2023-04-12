import requests
from selenium import webdriver


class Drivers:
    def __init__(self):
        self.driver = None

    def drivers(self, windowsId, tableName, align=None):
        if tableName == 'ads_task':
            url = 'http://local.adspower.net:50325/api/v1/browser/'
            open_url = url + 'start?user_id=' + windowsId + '&open_tabs=1'
            resp = requests.get(open_url).json()
            chrome_driver = resp["data"]["webdriver"]
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
            self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            self.driver.set_page_load_timeout(120)
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                    for (let key in window) {
                        if ((key.indexOf('ads_ado') != -1)
                        || (key.indexOf('ethereum') != -1)
                        || (key.indexOf('SENTRY_RELEASE') != -1)
                        || (key.indexOf('SENTRY_RELEASES') != -1)
                        || (key.indexOf('__SENTRY__') != -1)) {
                            delete window[key]
                        }
                    }
                """})
            # 防止网站检测selenium的webdriver
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => False
                    })
                """})
        elif tableName == 'bit_task':
            headers = {'id': windowsId, 'loadExtensions': True}
            openurl = "http://127.0.0.1:54345/browser/open"
            resp = requests.session().post(openurl, json=headers).json()
            chrome_driver = r"D:\\chromedriver.exe"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("debuggerAddress", resp['data']['http'])
            self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            self.driver.set_page_load_timeout(120)
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                    for (let key in window) {
                        if ((key.indexOf('bit_Qm') != -1)
                        || (key.indexOf('ethereum') != -1)
                        || (key.indexOf('SENTRY_RELEASE') != -1)
                        || (key.indexOf('SENTRY_RELEASES') != -1)
                        || (key.indexOf('__SENTRY__') != -1)) {
                            delete window[key]
                        }
                    }
                """})
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
