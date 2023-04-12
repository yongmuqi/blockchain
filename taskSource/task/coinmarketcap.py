import base64
import random
import time
import cv2
import numpy as np
import pyautogui
from selenium.webdriver.common.by import By
from taskSource.method import elementMethod, Mysql
from taskSource.task import Wallet


class CoinMarketCap:
    def __init__(self, driver):
        self.driver = driver
        self.drivers = elementMethod(driver)
        self.wallet = Wallet(driver)
        self.mysql = Mysql()

    def screenshot(self):
        img = self.driver.get_screenshot_as_base64()
        # 将 Base64 编码的字符串解码为二进制数据
        binary_data = base64.b64decode(img)

        img_np = np.frombuffer(binary_data, dtype=np.uint8)
        captcha_img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

        # 对验证码图片进行二值化和边缘检测
        captcha_img = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2GRAY)

        bg_edge = cv2.Canny(captcha_img, 100, 200)
        tp_edge = cv2.Canny(cv2.imread(r'D:\Documents\Pycharm\adsTask\taskSource\image\coinmarketcap\t3.png'), 100, 200)

        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        slider = self.drivers.element_Wait.wait_visibility_of_element_t(By.XPATH, "//div[@_id='slth']", 20)
        distance = max_loc[0] - slider.location['x']
        self.slide_by_pyautogui(slider.location['x'], slider.location['y'], distance)

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

    # 钻石登陆
    def LoginToCollect(self, Num, tableName):
        try:
            self.drivers.element_Action.click("//button[text()='Log In to Collect']")
            time.sleep(3)
            self.drivers.element_Action.click("(//button[text()='Log In'])[2]")
            loginSuccess = self.drivers.element_Action.get_text_t(By.XPATH, "//div[text()='You have successfully logged in!']", 20)
            self.CollectDiamonds(Num, tableName)
        except BaseException:
            self.mysql.add(tableName, 'CoinMarketcap', '登录失败', Num)
            time.sleep(1)

    # 钻石签到
    def CollectDiamonds(self, Num, tableName):
        self.drivers.element_Browser.maxWindows()
        self.drivers.element_Browser.navi_to_page("https://coinmarketcap.com/account/my-diamonds/")
        time.sleep(3)
        try:
            self.drivers.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Log In to Collect']", 3)
            self.LoginToCollect(Num, tableName)
        except BaseException:
            pass
        # try:
        notion = self.drivers.element_Action.get_text("//button[@data-page='diamondsPage']")
        if 'Collect Diamonds' in notion:
            DiamondsCount = self.drivers.element_Action.get_text("//span[@class='notranslate']")
            if int(DiamondsCount) == 0:
                self.drivers.element_Browser.refresh()
            self.drivers.element_Action.click("//button[text()='Collect Diamonds']")
            self.drivers.element_Wait.wait_visibility_of_element_t(By.XPATH, "//div[@_id='shim']", 20)
            time.sleep(3)
            self.screenshot()
            time.sleep(3)
            try:
                notion = self.drivers.element_Action.get_text_t(By.XPATH, "//div[@class='sc-b02c45e6-0 hDfmyu']//p[1]", 5)
            except BaseException:
                self.drivers.element_Action.click("//*[@class='bs-refresh-icon']")
                time.sleep(5)
                self.screenshot()
                time.sleep(2)
                notion = self.drivers.element_Action.get_text_t(By.XPATH, "//div[@class='sc-b02c45e6-0 hDfmyu']//p[1]", 20)
            self.mysql.add(tableName, 'CoinMarketcap', '领取成功', Num)
            time.sleep(1)
        elif 'to collect' in notion:
            self.mysql.add(tableName, 'CoinMarketcap', '已经领取', Num)
            time.sleep(1)
