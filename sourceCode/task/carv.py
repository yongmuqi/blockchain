import time
from playwright.sync_api import Page, Browser
from sourceCode.method.wallet import Wallet
from sourceCode.method.mysql import Mysql


class Carv:
    def __init__(self, page, browser):
        self.page: Page = page
        self.browser: Browser = browser
        self.wallet = Wallet(self.page, self.browser)
        self.mysql = Mysql()

    def carv_task(self, Num, tableName):
        self.page.goto('https://carv.io/account/quests')
        time.sleep(5)
        try:
            self.carv_logout()
            self.carv_checkin(Num, tableName)
        except BaseException:
            self.carv_checkin(Num, tableName)

    def carv_checkin(self, Num, tableName):
        button = self.page.locator("//span[text()='Check in']/..")
        disabled = button.get_attribute("disabled")
        if disabled is not None:
            self.mysql.add(tableName, 'Carv', '领取成功', Num)
        else:
            self.page.click("//span[text()='Check in']")
            self.page.wait_for_selector("//div[@role='alert']//div", timeout=10000)
            try:
                notion = self.page.text_content("//span[contains(@class,'inline-block w-14')]")
                self.mysql.add(tableName, 'Carv', '领取成功', Num)
            except BaseException:
                self.mysql.add(tableName, 'Carv', '领取失败', Num)

    def carv_logout(self):
        try:
            self.page.wait_for_selector("//div[@role='alert']//div", timeout=3000)
            self.page.hover("//img[@alt='avatar']")
            self.page.click("//button[text()='Log out']")
            self.page.reload()
            self.carv_login()
        except BaseException:
            self.carv_login()

    def carv_login(self):
        try:
            self.page.hover("//button[contains(@class,'bg-blue-700 rounded')]", timeout=3000)
            self.page.click("//span[text()='Ethereum']", timeout=2000)
            self.page.evaluate('document.querySelector("body > onboard-v2").shadowRoot.querySelector("section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-ro440k > div.scroll-container.svelte-ro440k > div.svelte-ro440k > div > div > button:nth-child(1) > span").click()')
            self.wallet.metamask_sign()
            self.page.goto('https://carv.io/account/quests')
            time.sleep(3)
        except BaseException:
            pass
