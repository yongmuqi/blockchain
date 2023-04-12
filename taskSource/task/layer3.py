import time

from selenium.webdriver.common.by import By
from taskSource.method import Mysql
from taskSource.method import elementMethod
from .wallet import Wallet


class Layer3:
    def __init__(self, driver):
        self.driver = elementMethod(driver)
        self.mysql = Mysql()
        self.wallet = Wallet(driver)

    def layer3Task(self, Num, tableName):
        self.driver.element_Browser.navi_to_page('https://layer3.xyz/quests')
        time.sleep(3)
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//button[@aria-haspopup="menu"]', 3)
            self.layer3_Sign(Num, tableName)
        except BaseException:
            self.driver.element_Action.click("//span[text()='Sign in']")
            self.driver.element_Action.click("//span[text()='Metamask']")
            self.wallet.metaMask_FirstSign()
            self.layer3_Sign(Num, tableName)

    def layer3_Sign(self, Num, tableName):
        try:
            try:
                self.driver.element_Action.click_t(By.XPATH, "//button[text()='gm']", 3)
            except BaseException:
                self.driver.element_Action.click_t(By.XPATH, "(//button[text()='gm'])[2]", 3)
            notion = self.driver.element_Action.get_text("//span[contains(@class,'c-hDdBLZ c-hDdBLZ-jawnKF-color-primary')]")
            self.mysql.add(tableName, 'Layer3', notion+' day gm streak!', Num)
        except BaseException:
            self.mysql.add(tableName, 'Layer3', '还没到领取时间', Num)
