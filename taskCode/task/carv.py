import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query
from selenium.webdriver import Keys
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
    carv_stateSuccess = 'CARV领取成功'
    carv_stateFail = '失败'
    carv_Dragonball_success = '龙珠碎片领取成功'
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
    def carv_checkin(self, adsNum):
        # 打开https://carv.io/account/quests页面
        self.driver.browser.navi_to_page(self.carv_url)
        time.sleep(5)
        try:
            # 定位头像元素，如果存在则是登录状态，执行签到任务，不存在执行登录操作
            self.driver.find.xpath_element(self.carv_img)
            # 定位check-in按钮，如果可以点击则点击并写入EXCEL，如果不能点击则继续
            self.driver.element.click(self.carv_checkin_xpath)
            time.sleep(5)
            button = self.driver.element.get_is_enabled(self.carv_checkin_button_xpath)
            if button:
                self.q.add(self.taskName, self.carv_stateFail, adsNum)
            elif not button:
                self.q.add(self.taskName, self.carv_stateSuccess, adsNum)
        except BaseException:
            # 执行登录操作
            self.carv_login(adsNum)

    def carv_login(self, adsNum):
        # 鼠标移动并悬停在login-button按钮
        self.driver.mouse.move_on_element(self.carv_login_button_xpath)
        # 点击ethereum按钮，并等待3秒
        self.driver.element.click(self.carv_ethereum_button_xpath)
        time.sleep(3)
        # 定义TAB次数为16次，如果有Check-in按钮，则TAB次数为12次
        count = 17
        try:
            self.driver.find.xpath_element(self.carv_checkin_button_xpath)
        except BaseException:
            count = 13
        for x in range(count):
            self.driver.mouse.keyboard_element(Keys.TAB)
        # 点击ENTER按钮，等待5秒，等待metamask页面的出现
        self.driver.mouse.keyboard_element(Keys.ENTER)
        time.sleep(5)
        # 切换到metamask页面执行登录功能
        self.wallet.metamask_sign()
        # 执行carv签到任务
        self.carv_checkin(adsNum)

    # carv领取龙珠碎片功能
    def carv_Dragonball(self, adsNum):
        # 打开领取龙珠碎片的页面
        self.driver.browser.navi_to_page(self.carv_Dragonball_url)
        time.sleep(10)
        # 如果存在碎片，则点击领取并写入EXCEL，如果没有碎片，则写入领取失败
        try:
            self.driver.element.click(self.carv_Dragonball_COLLECT)
            self.q.add(self.taskName1, self.carv_Dragonball_success, adsNum)
            time.sleep(5)
        except BaseException:
            self.q.add(self.taskName1, self.carv_Dragonball_fail, adsNum)
