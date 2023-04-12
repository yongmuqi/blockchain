import time
from selenium.webdriver.common.by import By
from taskSource.method import elementMethod, Config
from taskSource.method import Mysql
from taskSource.config import carvUrl
from taskSource.task.wallet import Wallet
from taskSource.function.textFile import textFile


class Carv:
    # 数据库表名
    taskName = 'Carv'

    def __init__(self, driver):
        self.driver = elementMethod(driver)
        self.wallet = Wallet(driver)
        self.mysql = Mysql()

    def carvTask(self, Num, tableName):
        self.driver.element_Browser.navi_to_page("https://carv.io/account/quests")
        time.sleep(5)
        try:
            self.carv_Login()
        except BaseException:
            pass
        self.carv_CheckIn(Num, tableName)

    def carv_CheckIn(self, Num, tableName):
        self.driver.element_Action.click("//span[text()='Check in']")
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "/div[text()='Check in done!']", 15)
            self.mysql.add(tableName, 'Carv', '领取成功', Num)
        except BaseException:
            self.mysql.add(tableName, 'Carv', '失败', Num)

    def carv_Login(self):
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//div[@role='alert']//div", 3)
        except BaseException:
            pass
        self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[contains(@class,'bg-blue-700 rounded')]", 5)
        # 鼠标移动并悬停在login-button按钮
        self.driver.element_Mouse.move_on_element("//button[contains(@class,'bg-blue-700 rounded')]")
        # 点击ethereum按钮，并等待3秒
        self.driver.element_Action.click("//span[text()='Ethereum']")
        time.sleep(3)
        # 通过JS点击metamask的按钮（shadowRoot）
        self.driver.element_Wait.wait_execute_script(
            'document.querySelector("body > onboard-v2").shadowRoot.querySelector("section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-ro440k > div.scroll-container.svelte-ro440k > div.svelte-ro440k > div > div > button:nth-child(1) > span").click()')
        time.sleep(5)
        self.wallet.metaMask_Sign()
        self.driver.element_Browser.navi_to_page("https://carv.io/account/account")
        time.sleep(3)
        print('1')
        self.driver.element_Action.click('//div[@class="w-full mt-5 mb-4"]/../menu/a[2]')
        print('2')
        time.sleep(1)

    # carv领取龙珠碎片功能
    def carv_Dragonball(self, Num, tableName):
        # 打开领取龙珠碎片的页面
        self.driver.element_Browser.navi_to_page("https://carv.io/account/quests")
        time.sleep(5)
        try:
            self.driver.element_Action.click('//*[@id=":r0:"]/span[1]')
            self.mysql.add(tableName, 'CarvDragonball', '龙珠碎片领取成功', Num)
            time.sleep(5)
        except BaseException:
            self.mysql.add(tableName, 'CarvDragonball', '领取失败', Num)

    # 获取carv账户网址，用作互相关注
    def carv_Url(self, Num):
        self.driver.element_Browser.navi_to_page("https://carv.io/account/quests")
        time.sleep(5)
        try:
            self.driver.element_Action.click("//div[@class='h-14 flex items-center mx-4']")
        except BaseException:
            pass
        self.driver.element_Action.click("(//span[text()='Profile'])[2]")
        url = self.driver.element_Browser.current_url()
        textFile.write_txt_data(str(Num) + ':' + url)

    # carv互关
    def carv_Follow(self):
        all_bitNum = Config.all_bit()
        for i in range(1, len(all_bitNum) + 1):
            url = carvUrl.carvUrl[i]
            self.driver.element_Browser.navi_to_page(url)
            self.driver.element_Wait.wait_visibility_of_element('//*[@class="text-white text-xl mr-2"]')
            try:
                self.driver.element_Action.click_t(By.XPATH, "//button[text()=' Follow']", 3)
                self.driver.element_Function.wait_for_text_change('//button[@class="text-gray-400 text-xs"]')
            except BaseException:
                pass
