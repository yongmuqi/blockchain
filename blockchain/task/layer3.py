import time
from selenium.webdriver.common.by import By
from blockchain.method import Method
from .wallet import Wallet


class Layer3:
    def __init__(self, driver):
        self.driver = Method(driver)
        self.wallet = Wallet(driver)

    def layer3Task(self, Num, tableName):
        self.driver.browser.navi_to_page('https://layer3.xyz/quests')
        time.sleep(3)
        try:
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, '//button[@aria-haspopup="menu"]', 3)
            self.layer3_Sign(Num, tableName)
        except BaseException:
            self.driver.element.click("//span[text()='Sign in']")
            self.driver.element.click("//span[text()='Metamask']")
            self.wallet.metaMask_FirstSign()
            self.layer3_Sign(Num, tableName)

    def layer3_Sign(self, Num, tableName):
        try:
            try:
                self.driver.element.click_t(By.XPATH, "//button[text()='gm']", 3)
            except BaseException:
                self.driver.element.click_t(By.XPATH, "(//button[text()='gm'])[2]", 3)
            notion = self.driver.element.get_text("//span[contains(@class,'c-hDdBLZ c-hDdBLZ-jawnKF-color-primary')]")
            self.driver.mysql.add(tableName, 'Layer3', notion+' day gm streak!', Num)
        except BaseException:
            self.driver.mysql.add(tableName, 'Layer3', '还没到领取时间', Num)
