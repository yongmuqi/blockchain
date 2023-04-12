import time
from playwright.sync_api import Page, Browser
from sourceCode.method.config import Config
from sourceCode.method.function import Function
from sourceCode.method.wallet import Wallet
from sourceCode.method.mysql import Mysql


class Coingecko:
    def __init__(self, page, browser):
        self.page: Page = page
        self.browser: Browser = browser
        self.wallet = Wallet(self.page, self.browser)
        self.mysql = Mysql()

    def coingecko_task(self, Num, tableName):
        self.page.goto('https://www.coingecko.com/account/candy?locale=zh')
        time.sleep(5)
        try:
            self.coingecko_checkin(Num, tableName)
        except BaseException:
            self.coingecko_login()
            self.coingecko_checkin(Num, tableName)

    def coingecko_checkin(self, Num, tableName):
        try:
            self.page.click("(//button[@type='submit'])[2]", timeout=3000)
            time.sleep(3)
            self.page.reload()
            notion = '本次：' + self.page.text_content("//div[contains(@class,'col-8 col-lg-10')]//span")
            self.mysql.add(tableName, 'CoinGecko', notion, Num)
        except BaseException:
            next_time = '下次领取：' + self.page.text_content("(//div[contains(@class,'btn bg-secondary')]//span)[2]")
            self.mysql.add(tableName, 'CoinGecko', next_time, Num)

    def coingecko_login(self):
        pass

    def cassava_task(self, Num, tableName):
        self.page.goto('https://app.cassava.network/#/')
        time.sleep(3)
        try:
            self.page.wait_for_selector("//i[@class='iconfont icon-checkin']", timeout=3000)
        except BaseException:
            self.cassava_login(Num, tableName)
        self.page.click("//i[@class='iconfont icon-checkin']")
        notion = self.page.text_content("//div[@class='my-message']//span[1]", timeout=10000)
        self.mysql.add(tableName, 'Cassava', notion, Num)

    def cassava_login(self, Num, tableName):
        password = Config.password_next()
        if tableName == 'ads_task':
            mail = Config.adsMail(Num)
        else:
            mail = Config.bitMail(Num)
        try:
            self.page.click('//button[@class="btn btn-default btn-small btn-transparent loginBtn"]')
            loginPage = Function(self.page, self.browser).wait_for_new_popup("UniPass")
            loginPage.fill('//input[@placeholder="Please enter your email address"]', mail)
            loginPage.click("//span[text()='Log in']")
            loginPage.click("//span[text()='Continue with Google']")
            loginPage.wait_for_load_state("load")
            loginPage.click('//div[@class="w1I7fb"]')
            loginPage.fill('//input[@placeholder="Please enter password"]', password)
            loginPage.click("//span[text()='Log in']")
            loginPage.click("//span[text()='Sign in']")
            self.page.wait_for_selector("//i[@class='iconfont icon-checkin']")
        except BaseException:
            self.mysql.add(tableName, 'Cassava', '登录失败', Num)

    def soquestTask(self, Num, tableName):
        self.wallet.metamask_switch_mainnet()
        self.page.goto("https://soquest.xyz/privilege")
        time.sleep(2)
        try:
            self.page.wait_for_selector('//*[@alt="notification"]', timeout=3000)
        except BaseException:
            self.page.click('//button[text()="Connect Wallet"]')
            self.page.click('//span[text()="MetaMask"]')
            self.wallet.metamask_sign()
        self.page.click('//div[@class="mui-style-1w0q4w9"]/button')
        time.sleep(2)
        notion = self.page.text_content("//button[text()='Collect Tomorrow']")
        self.mysql.add(tableName, 'Soquest', notion, Num)
