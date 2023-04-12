import datetime
import time

from selenium.webdriver.common.by import By
from taskSource.method import Mysql
from taskSource.method import elementMethod
from .wallet import Wallet


class Zetalabs:
    def __init__(self, driver):
        self.driver = elementMethod(driver)
        self.wallet = Wallet(driver)
        self.mysql = Mysql()

    def zetaTask(self, Num, tableName):
        self.driver.element_Browser.navi_to_page('https://labs.zetachain.com/get-zeta')
        try:
            notion = self.driver.element_Action.get_text_t(By.XPATH, "//div[@class='css-1dekv6v e8ks3x80']//p[1]", 5)
            if 'Network' in notion:
                self.mysql.add(tableName, 'Zetalabs', 'zeta正在维护', Num)
        except BaseException:
            self.zeta_getToken(Num, tableName)
            time.sleep(3)
            swapRunDay = datetime.datetime.now()
            if swapRunDay.isoweekday() == 5:
                # 点击try-swapping按钮进行SWAP操作
                self.zeta_swap(Num, tableName)

    def zeta_getToken(self, Num, tableName):
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Request Assets']", 15)
            try:
                self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Try Swapping!']", 20)
                self.mysql.add(tableName, 'Zetalabs', '测试币领取成功', Num)
            except BaseException:
                self.mysql.add(tableName, 'Zetalabs', "领取失败", Num)
        except BaseException:
            next_time = self.driver.element_Action.get_text("(//p[contains(@class,'MuiTypography-root MuiTypography-body1')]/following-sibling::p)[2]")
            wait_times = {
                '0 minute': 60,
                '1 minute': 120,
                '2 minutes': 180,
            }
            if next_time in wait_times:
                self.request_assets(wait_times[next_time], Num, tableName)
            else:
                self.mysql.add(tableName, 'Zetalabs', next_time, Num)
            # next_time = self.driver.element_Action.get_text("(//p[contains(@class,'MuiTypography-root MuiTypography-body1')]/following-sibling::p)[2]")
            # if next_time == '0 minute':
            #     time.sleep(60)
            #     self.driver.element_Browser.refresh()
            #     self.driver.element_Action.click_t(By.XPATH, "//button[text()='Request Assets']", 15)
            #     self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Try Swapping!']", 20)
            #     self.mysql.add(tableName, 'Zetalabs', '测试币领取成功', Num)
            # elif next_time == '1 minute':
            #     time.sleep(120)
            #     self.driver.element_Browser.refresh()
            #     self.driver.element_Action.click_t(By.XPATH, "//button[text()='Request Assets']", 15)
            #     self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Try Swapping!']", 20)
            #     self.mysql.add(tableName, 'Zetalabs', '测试币领取成功', Num)
            # elif next_time == '2 minutes':
            #     time.sleep(180)
            #     self.driver.element_Browser.refresh()
            #     self.driver.element_Action.click_t(By.XPATH, "//button[text()='Request Assets']", 15)
            #     self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Try Swapping!']", 20)
            #     self.mysql.add(tableName, 'Zetalabs', '测试币领取成功', Num)
            # else:
            #     self.mysql.add(tableName, 'Zetalabs', next_time, Num)

    def request_assets(self, wait_time, Num, tableName):
        time.sleep(wait_time)
        self.driver.element_Browser.refresh()
        self.driver.element_Action.click_t(By.XPATH, "//button[text()='Request Assets']", 15)
        self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Try Swapping!']", 20)
        self.mysql.add(tableName, 'Zetalabs', '测试币领取成功', Num)

    def zeta_swap(self, Num, tableName):
        self.driver.element_Browser.navi_to_page('https://labs.zetachain.com/swap')
        time.sleep(5)
        swapTime = self.driver.element_Action.get_text_t(By.XPATH, "//div[contains(@class,'flex flex-row-reverse')]//p[1]", 20)
        if 'Swap now' in swapTime:
            try:
                self.driver.element_Action.click_t(By.XPATH, '//button[@class="css-kjyh70 ecs3q253"]', 3)
            except BaseException:
                self.driver.element_Action.click("//p[text()='Select Network']")
            time.sleep(0.5)
            try:
                self.driver.element_Action.click_t(By.XPATH, "(//p[text()='Polygon Mumbai'])[2]", 3)
            except BaseException:
                self.driver.element_Action.click("(//p[text()='Polygon Mumbai'])")
            time.sleep(0.5)
            self.driver.element_Action.click("//p[text()='Select Token']")
            time.sleep(0.5)
            self.driver.element_Action.click("//p[text()='ZETA']")
            time.sleep(0.5)
            self.driver.element_Action.click("//p[text()='Select Network']")
            time.sleep(0.5)
            self.driver.element_Action.click("//p[text()='BSC Testnet']")
            time.sleep(0.5)
            self.driver.element_Action.click("//p[text()='Select Token']")
            time.sleep(0.5)
            self.driver.element_Action.click("(//p[text()='ZETA'])[2]")
            time.sleep(2)
            self.driver.element_Action.send_keys("//input[contains(@class,'sm:text-left text-right')]", '3')
            time.sleep(3)
            review = self.driver.element_Action.get_text_t(By.XPATH, "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[3]", 20)
            if review == 'Review Order':
                self.driver.element_Action.click("//button[text()='Review Order']")
            else:
                self.driver.element_Action.click("(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[3]")
                self.wallet.metaMask_SwitchNetWork()
                self.driver.element_Action.click("//button[text()='Review Order']")
            time.sleep(5)
            swap = self.driver.element_Action.get_text_t(By.XPATH, "(//div[@class='css-yu1lbc egmuoqj0']//button)[2]", 20)
            if swap == 'Swap':
                self.driver.element_Action.click("//button[text()='Swap']")
            else:
                self.driver.element_Function.wait_and_click_button("//button[text()='Allow ZETA Transfer']")
                self.wallet.metaMask_Submit_sendCustom()
                # 判断swap按钮是否可点击，一直等待到swap按钮返回True（可点击）为止
                self.driver.element_Function.wait_and_click_button("//button[text()='Swap']")
            self.wallet.metaMask_Submit()
            # 获取SWAP成功后的通知文本，并写入EXCEL
            notion = self.driver.element_Action.get_text_t(By.XPATH, '//div[@class="MuiAlert-message css-1w0ym84"]', 60)
            self.mysql.add(tableName, 'Zetalabs', 'swap成功', Num)
            time.sleep(5)
        else:
            self.mysql.add(tableName, 'Zetalabs', swapTime, Num)
