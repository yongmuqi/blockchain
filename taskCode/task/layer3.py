import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query
from .wallet import Wallet


class Layer3:
    layer3_url = 'https://beta.layer3.xyz/contests'
    layer3_sign = "//button[@class='c-gwBWWG c-gwBWWG-iiNvmaL-css']"
    layer3_notion = "//p[contains(@class,'c-iKqlBJ c-iKqlBJ-fAKXXr-size-sm')]"
    layer3_metamask = "//div[text()='Metamask']"
    layer3_metamaskLogin = "//span[text()='Connect wallet']"
    layer3_metamaskButton = '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]'
    layerMessage = 'layer3还没到签到时间'
    # 数据库表头
    taskName = 'Layer3'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)
        self.q = Query()

    def layer3(self, adsNum):
        self.driver.browser.navi_to_page(self.layer3_url)
        time.sleep(5)
        try:
            self.driver.element.click(self.layer3_metamaskLogin)
            self.driver.element.click(self.layer3_metamask)
            time.sleep(3)
            self.wallet.metamask_sign()
            self.driver.element.click(self.layer3_sign)
            time.sleep(5)
            notion = self.driver.element.get_text(self.layer3_notion)
            self.q.add(self.taskName, notion, adsNum)
        except BaseException:
            try:
                self.driver.element.click(self.layer3_sign)
                time.sleep(5)
                notion = self.driver.element.get_text(self.layer3_notion)
                self.q.add(self.taskName, notion, adsNum)
            except BaseException:
                self.q.add(self.taskName, self.layerMessage, adsNum)
