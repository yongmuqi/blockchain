import base64
import random
import time
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from playwright.sync_api import Page, Browser
from sourceCode.method.wallet import Wallet
from sourceCode.method.mysql import Mysql


class Coinmarketcap:
    def __init__(self, page, browser):
        self.page: Page = page
        self.browser: Browser = browser
        self.wallet = Wallet(self.page, self.browser)
        self.mysql = Mysql()

    def screenshot(self):
        img = self.page.screenshot()
        # 将 Base64 编码的字符串解码为二进制数据
        binary_data = base64.b64decode(img)

        img_np = np.frombuffer(binary_data, dtype=np.uint8)
        captcha_img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

        # 对验证码图片进行二值化和边缘检测
        captcha_img = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2GRAY)

        bg_edge = cv2.Canny(captcha_img, 100, 200)
        tp_edge = cv2.Canny(cv2.imread(r'D:\Documents\Pycharm\adsTask\sourceCode\image\coinmarketcap\t3.png'), 100, 200)

        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        slider = self.page.locator("//div[@_id='slth']")
        distance = max_loc[0] - slider.bounding_box()['x']
        self.slide_by_pyautogui(slider.bounding_box()['x'], slider.bounding_box()['y'], distance)

    @staticmethod
    def slide_by_pyautogui(x, y, offset):
        """
        slide by pyautogui
        :param x: X轴起始位置
        :param y: Y轴起始位置
        :param offset: 实际移动距离
        """
        xx = x + offset
        pyautogui.moveTo(x, y, duration=2.3)
        pyautogui.mouseDown()
        y += random.randint(9, 19)
        pyautogui.moveTo(x + int(offset * random.randint(15, 23) / 20), y, duration=2.4)
        y += random.randint(-9, 0)
        pyautogui.moveTo(x + int(offset * random.randint(17, 21) / 20), y, duration=(random.randint(20, 31)) / 100)
        pyautogui.moveTo(xx, y, duration=1.8)
        pyautogui.mouseUp()

    def coinmarketcap_task(self, Num, tableName):
        all = gw.getAllTitles()
        for a in all:
            print(a)
            if 'SunBrowser' in a:
                window = gw.getWindowsWithTitle(a)[0]
                window.maximize()

        self.page.goto('https://coinmarketcap.com/account/my-diamonds/')
        time.sleep(3)
        try:
            self.page.wait_for_selector("//button[text()='Log In to Collect']", timeout=3000)
            self.coinmarketcap_login(Num, tableName)
        except BaseException:
            pass
        button = self.page.text_content("//button[@data-page='diamondsPage']")
        if 'Collect Diamonds' in button:
            DiamondsCount = self.page.text_content("//span[@class='notranslate']")
            if int(DiamondsCount) == 0:
                self.page.reload()
            self.page.click("//button[text()='Collect Diamonds']")
            self.page.wait_for_selector("//div[@_id='shim']", timeout=20000)
            time.sleep(3)
            self.screenshot()
            time.sleep(3)
            try:
                self.page.wait_for_selector("//div[@class='sc-b02c45e6-0 hDfmyu']//p[1]", timeout=10000)
            except BaseException:
                self.page.click("//*[@class='bs-refresh-icon']")
                time.sleep(5)
                self.screenshot()
                time.sleep(2)
                self.page.wait_for_selector("//div[@class='sc-b02c45e6-0 hDfmyu']//p[1]", timeout=10000)
            self.mysql.add(tableName, 'CoinMarketcap', '领取成功', Num)
        elif 'to collect' in button:
            self.mysql.add(tableName, 'CoinMarketcap', '已经领取', Num)

    def coinmarketcap_login(self, Num, tableName):
        try:
            self.page.click("//button[text()='Log In to Collect']")
            time.sleep(3)
            self.page.click("(//button[text()='Log In'])[2]")
            self.page.wait_for_selector("//div[text()='You have successfully logged in!']", timeout=20000)
        except BaseException:
            self.mysql.add(tableName, 'CoinMarketcap', '登录失败', Num)
            time.sleep(1)
