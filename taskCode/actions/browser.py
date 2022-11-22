import time

import requests


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
        self.driver.switch_to.window(all_handles[0])

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
