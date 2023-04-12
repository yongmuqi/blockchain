import time
from playwright.sync_api import Page, Browser
from sourceCode.method.mysql import Mysql
from sourceCode.method.function import Function


class Wallet:
    def __init__(self, page, browser):
        self.page: Page = page
        self.browser: Browser = browser
        self.mysql = Mysql()
        self.password = self.mysql.search_db('others', 1)[1]

    def metamask_login(self, Num, tableName):
        self.page.goto('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        time.sleep(3)
        try:
            self.page.wait_for_selector('//div[@class="spinner loading-overlay__spinner"]', timeout=3000)
            self.page.click('//button[@class="button btn--rounded btn-secondary"]', timeout=30000)
            self.page.click("//span[text()='Ethereum Mainnet']")
        except BaseException:
            pass
        try:
            self.page.wait_for_selector('//*[@id="password"]', timeout=5000)
            self.page.fill('//*[@id="password"]', self.password)
        except BaseException:
            self.page.reload()
            self.page.fill('//*[@id="password"]', self.password)
        self.page.click('//button[@data-testid="unlock-submit"]')
        self.mysql.add(tableName, 'MetaMask', 'MetaMask登录成功', Num)
        try:
            self.page.click("//button[text()='Got it']", timeout=3000)
        except BaseException:
            pass
        try:
            self.page.click("//button[text()='Reject']", timeout=3000)
        except BaseException:
            pass

    # 切换到ETH主网
    def metamask_switch_mainnet(self):
        self.page.goto('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        self.page.click('//div[@class="chip__right-icon"]')
        self.page.click('//span[@data-testid="mainnet-network-item"]')

    def metamask_sign(self):
        metamaskPage = Function(self.page, self.browser).wait_for_new_popup("MetaMask")
        metamaskPage.click('//button[@data-testid="page-container-footer-next"]')
        time.sleep(3)