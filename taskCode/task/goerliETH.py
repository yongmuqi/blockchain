import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query


class GoerliETH:
    # goerli-token页面元素
    goerli_url = 'https://goerlifaucet.com/'
    goerLi_timeOut = 'goerliETH还没到领取时间'
    goerLi_fail = '领取失败'
    goerLi_success = 'goerliETH领取成功'
    goerLi_wrong = '其他错误'
    goerli_login_button = "//button[contains(@class,'btn btn-outline-light')]"
    goerli_input = "//input[@type='address']"
    goerli_SendMeETH = "//span[text()='Send Me ']"
    goerli_message = "//div[@role='alert']"
    goerli_account_login = "//button[text()='Sign in']"
    # 数据库表头
    taskName = 'GoerliETH'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.q = Query()

    # 领取goerli-token测试币功能
    def goerli_token(self, adsAddress, adsNum):
        # 打开goerli-token的页面
        self.driver.browser.navi_to_page(self.goerli_url)
        time.sleep(15)
        self.driver.find.xpath_element(self.goerli_login_button)
        # 如果右上角按钮显示“Logout”，则进行领取操作，如果不是，则进行登录操作
        if self.driver.element.get_text(self.goerli_login_button) == 'Logout':
            # 输入框输入metamask钱包的地址，并点击领取
            self.driver.element.send_keys(self.goerli_input, adsAddress)
            self.driver.element.click(self.goerli_SendMeETH)
            try:
                # 定义notion为领取后的通知文本，不同内容对应不同的EXCEL输出
                notion = self.driver.element.get_text(self.goerli_message)
                if 'Sorry!' in notion:
                    self.q.add(self.taskName, self.goerLi_timeOut, adsNum)
                elif 'reCAPTCHA' in notion:
                    self.q.add(self.taskName, self.goerLi_fail, adsNum)
                else:
                    self.q.add(self.taskName, self.goerLi_wrong, adsNum)
            except BaseException:
                self.q.add(self.taskName, self.goerLi_success, adsNum)
        else:
            # 执行登录操作
            self.goerli_login(adsAddress, adsNum)

    # goerli-login登录功能
    def goerli_login(self, adsAddress, adsNum):
        # 点击右上角的登录按钮
        self.driver.element.click(self.goerli_login_button)
        time.sleep(10)
        # 点击通过GOOGLE按钮登录
        self.driver.element.click(self.goerli_account_login)
        time.sleep(10)
        # 执行领取goerli-token操作
        self.goerli_token(adsAddress, adsNum)
