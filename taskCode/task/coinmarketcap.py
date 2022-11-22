import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query


class Coinmarketcap:
    # coinmarketcap领取钻石任务
    coinmarketcap_url = 'https://coinmarketcap.com/account/my-diamonds/'
    coinmarketcap_login = "(//button[text()='Log In'])[2]"
    coinmarketcap_button = "//button[@data-page='diamondsPage']"
    # 数据库表头
    taskName = 'CoinMarketcap'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.q = Query()

    # coinmarketcap领取钻石功能
    def coinmarketcap_get(self, adsNum):
        # 打开coinmarketcap领取钻石页面
        self.driver.browser.navi_to_page(self.coinmarketcap_url)
        time.sleep(5)
        # 定义notion按钮，如果按钮为Collect Diamonds则点击领取钻石，如果按钮为Log In to Collect则执行登录操作
        notion = self.driver.element.get_text(self.coinmarketcap_button)
        if notion == 'Collect Diamonds':
            self.driver.element.click(self.coinmarketcap_button)
            time.sleep(5)
            self.driver.browser.refresh()
            time.sleep(5)
            notion = self.driver.element.get_text(self.coinmarketcap_button)
            self.q.add(self.taskName, notion, adsNum)
        elif notion == 'Log In to Collect':
            self.driver.element.click(self.coinmarketcap_button)
            time.sleep(10)
            self.driver.element.click(self.coinmarketcap_login)
            time.sleep(5)
            self.driver.element.click(self.coinmarketcap_button)
            time.sleep(5)
            self.driver.browser.refresh()
            time.sleep(5)
            notion = self.driver.element.get_text(self.coinmarketcap_button)
            self.q.add(self.taskName, notion, adsNum)
        else:
            self.q.add(self.taskName, notion, adsNum)
