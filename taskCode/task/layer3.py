import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query
from .wallet import Wallet


class Layer3:
    layer3_url = 'https://beta.layer3.xyz/bounties'
    layer3_sign = "//button[@class='c-gwBWWG c-gwBWWG-iiNvmaL-css']"
    layer3_notion = "//p[contains(@class,'c-iKqlBJ c-iKqlBJ-fAKXXr-size-sm')]"
    layer3_metamask = "//div[text()='Metamask']"
    layer3_metamaskLogin = "//span[text()='Connect wallet']"
    layer3_metamaskButton = '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]'
    layerMessage = '没到签到时间'
    # 数据库表头
    taskName = 'Layer3'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)
        self.q = Query()

    def layer3(self, adsNum, tableName):
        self.driver.browser.navi_to_page(self.layer3_url)
        time.sleep(5)
        try:
            self.driver.element.click_3sec(self.layer3_metamaskLogin)
            self.driver.element.click(self.layer3_metamask)
            time.sleep(3)
            self.wallet.metamask_sign()
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec(self.layer3_sign)
            time.sleep(5)
            notion = self.driver.element.get_text(self.layer3_notion)
            self.q.add(tableName, self.taskName, notion, adsNum)
        except BaseException:
            self.q.add(tableName, self.taskName, self.layerMessage, adsNum)

    def cassava(self, adsNum, tableName):
        self.driver.browser.navi_to_page("https://app.cassava.network/#/")
        time.sleep(5)
        try:
            self.driver.element.click_3sec("//button[text()='Login']")
            time.sleep(3)
            self.driver.element.click('//input[@placeholder="Please enter your email address"]')
            time.sleep(2)
            self.driver.element.click("//button[text()='Submit']")
            time.sleep(5)
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec('//input[@placeholder="Please enter your email address"]')
            time.sleep(2)
            self.driver.element.click("//button[text()='Submit']")
            time.sleep(5)
        except BaseException:
            pass
        self.driver.element.click("//i[@class='iconfont icon-checkin']")
        notion = self.driver.element.get_text("(//span[@class='text'])[2]")
        self.q.add(tableName, 'Cassava', notion, adsNum)

    def soquest(self, adsNum, tableName):
        self.driver.browser.navi_to_page("https://soquest.xyz/privilege")
        time.sleep(5)
        self.driver.element.click("(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[2]")
        time.sleep(2)
        notion = self.driver.element.get_text("//button[text()='Collect Tomorrow']")
        self.q.add(tableName, 'Soquest', notion, adsNum)
