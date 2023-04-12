import time

import requests
from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    def __init__(self, driver):
        self.driver = driver

    # 封装关闭浏览器功能
    def close_windows(self, close_url):
        self.driver.quit()
        requests.get(close_url)

    # 关闭页面
    def close(self):
        self.driver.close()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    def maxWindows(self):
        self.driver.maximize_window()

    def set_window_size(self):
        self.driver.set_window_size(380, 570)

        # 获取当前网址
    def current_url(self):
        url = self.driver.current_url
        return url

    # 封装打开页面功能
    def navi_to_page(self, url):
        self.driver.get(url)

    # 浏览器窗口切换功能
    def windows_toggle(self, x):
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[len(all_handles) - x])

    # 浏览器窗口切换到首页
    def windows_handles(self):
        all_handles = self.driver.window_handles
        print(all_handles)
        self.driver.switch_to.window(all_handles[0])
        print(self.driver.title)

    def windows_wallet(self):
        waitTime = 0
        while True:
            all_handles = self.driver.window_handles
            waitTime = waitTime + 1
            if len(all_handles) > 1:
                self.driver.switch_to.window(all_handles[-1])
                print(self.driver.title)
                break
            elif waitTime > 15:
                break
            else:
                time.sleep(1)

    # 关闭浏览器页面只剩1个
    def close_page(self):
        all_handles = self.driver.window_handles
        closeNum = len(all_handles) - 1
        for x in range(closeNum):
            self.close()
            time.sleep(1)
            self.windows_handles()

    # 封装截屏功能
    def screenshot(self, names):
        timestring = time.strftime('%Y-%m-%d-')
        self.driver.save_screenshot('image\\image' + timestring + names)
