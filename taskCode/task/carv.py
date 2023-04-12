import datetime
import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query
from .wallet import Wallet


class Carv:
    # carv签到页面元素
    carv_url = "https://carv.io/account/quests"
    carv_Dragonball_url = 'https://carv.io/events/dragonball'
    carv_Dragonball_COLLECT = '//*[@id=":r0:"]/span[1]'
    carv_img = "//img[@alt='avatar']"
    carv_notion = '//*[contains(@id,"__")]/div[1]/div[2]'
    carv_checkin_xpath = "//span[text()='Check in']"
    carv_checkin_button_xpath = "//button[contains(@class,'bg-blue-700 rounded')]"
    carv_stateSuccess = '签到成功'
    carv_stateFail = '失败'
    carv_Dragonball_success = '碎片领取成功'
    carv_Dragonball_fail = '领取失败'
    # carv登录页面元素
    carv_login_button_xpath = "//button[contains(@class,'bg-blue-700 rounded')]"
    carv_ethereum_button_xpath = "//span[text()='Ethereum']"
    # 数据库表名
    taskName = 'Carv'
    taskName1 = 'CarvDragonball'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)
        self.q = Query()

    # carv登录功能
    def carv_checkin(self, adsNum, tableName):
        # 打开https://carv.io/account/quests页面
        self.driver.browser.navi_to_page(self.carv_url)
        time.sleep(5)
        try:
            self.driver.find.xpath_element_3sec("//div[@role='alert']//div")
            self.driver.mouse.move_on_element(self.carv_img)
            time.sleep(1)
            self.driver.element.click("//button[text()='Log out']")
            time.sleep(3)
            self.driver.browser.refresh()
        except BaseException:
            pass
        try:
            self.carv_login()
        except BaseException:
            pass

        # 定位check-in按钮，如果可以点击则点击并写入EXCEL，如果不能点击则继续
        self.driver.element.click(self.carv_checkin_xpath)
        time.sleep(5)
        button = self.driver.element.get_is_enabled(self.carv_checkin_button_xpath)
        if button:
            self.q.add(tableName, self.taskName, self.carv_stateFail, adsNum)
        elif not button:
            self.q.add(tableName, self.taskName, self.carv_stateSuccess, adsNum)
        # # ADS账户每周二、五执行领取龙珠碎片任务
        # DragonballRunDay = datetime.datetime.now()
        # if DragonballRunDay.isoweekday() == 2:
        #     self.carv_Dragonball(adsNum, tableName)
        # elif DragonballRunDay.isoweekday() == 5:
        #     self.carv_Dragonball(adsNum, tableName)

    def carv_login(self):
        # 鼠标移动并悬停在login-button按钮
        self.driver.mouse.move_on_element(self.carv_login_button_xpath)
        # 点击ethereum按钮，并等待3秒
        self.driver.element.click_3sec(self.carv_ethereum_button_xpath)
        time.sleep(3)
        # 通过JS点击metamask的按钮（shadowRoot）
        self.driver.wait.wait_execute_script(
            'document.querySelector("body > onboard-v2").shadowRoot.querySelector("section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-ro440k > div.scroll-container.svelte-ro440k > div.svelte-ro440k > div > div > button:nth-child(1) > span").click()')
        time.sleep(10)
        self.wallet.metamask_sign()
        self.driver.browser.navi_to_page(self.carv_url)

    # carv领取龙珠碎片功能
    def carv_Dragonball(self, adsNum, tableName):
        # 打开领取龙珠碎片的页面
        self.driver.browser.navi_to_page(self.carv_Dragonball_url)
        time.sleep(10)
        # 如果存在碎片，则点击领取并写入EXCEL，如果没有碎片，则写入领取失败
        try:
            self.driver.element.click(self.carv_Dragonball_COLLECT)
            self.q.add(tableName, self.taskName1, self.carv_Dragonball_success, adsNum)
            time.sleep(5)
        except BaseException:
            self.q.add(tableName, self.taskName1, self.carv_Dragonball_fail, adsNum)
