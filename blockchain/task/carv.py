import time
from selenium.webdriver.common.by import By
from blockchain.method import Method
from .wallet import Wallet


class Carv:
    # 数据库表名
    taskName = 'Carv'

    def __init__(self, driver):
        self.driver = Method(driver)
        self.wallet = Wallet(driver)

    def carvTask(self, Num, tableName):
        self.driver.browser.navi_to_page("https://carv.io/account/quests")
        time.sleep(5)
        try:
            self.carv_Login()
        except BaseException:
            pass
        self.carv_CheckIn(Num, tableName)

    def carv_CheckIn(self, Num, tableName):
        self.driver.element.click("//span[text()='Check in']")
        try:
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, "/div[text()='Check in done!']", 15)
            self.driver.mysql.add(tableName, 'Carv', '领取成功', Num)
        except BaseException:
            self.driver.mysql.add(tableName, 'Carv', '失败', Num)

    def carv_Login(self):
        try:
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, "//div[@role='alert']//div", 3)
        except BaseException:
            pass
        self.driver.wait.wait_visibility_of_element_t(By.XPATH, "//button[contains(@class,'bg-blue-700 rounded')]", 5)
        # 鼠标移动并悬停在login-button按钮
        self.driver.mouse.move_on_element("//button[contains(@class,'bg-blue-700 rounded')]")
        # 点击ethereum按钮，并等待3秒
        self.driver.element.click("//span[text()='Ethereum']")
        time.sleep(3)
        # 通过JS点击metamask的按钮（shadowRoot）
        self.driver.wait.wait_execute_script(
            'document.querySelector("body > onboard-v2").shadowRoot.querySelector("section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-ro440k > div.scroll-container.svelte-ro440k > div.svelte-ro440k > div > div > button:nth-child(1) > span").click()')
        time.sleep(5)
        self.wallet.simple_sign()
        self.driver.browser.navi_to_page("https://carv.io/account/quests")
        time.sleep(3)
