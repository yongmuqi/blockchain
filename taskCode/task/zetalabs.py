import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query

from .wallet import Wallet


class Zetalabs:
    # zetalabs
    zetalabs_get_url = 'https://labs.zetachain.com/get-zeta'
    zetalabs_swap_url = 'https://labs.zetachain.com/swap'
    zetalabs_success = 'swap成功'
    zetalabs_getToken = '测试币领取成功'
    zetalabs_get_button = "//button[text()='Request Assets']"
    zetalabs_next_time = "(//p[contains(@class,'MuiTypography-root MuiTypography-body1')]/following-sibling::p)[2]"
    zetalabs_try_swapping = "//button[text()='Try Swapping!']"
    zetalabs_swapNetwork = "(//img[@alt='select'])[2]"
    zetalabs_swapToken = "(//img[@alt='select'])[3]"
    zetalabs_receiveNetwork = "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[3]"
    zetalabs_receiveToken = "(//button[@class='css-pshyj1 ecs3q253']/following-sibling::button)[2]"
    zetalabs_input = "//input[contains(@class,'sm:text-left text-right')]"
    zetalabs_review_button = "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[3]"
    zetalabs_empower_button = "(//div[@class='css-1x9yzpb egmuoqj0']//button)[2]"
    zetalabs_swap_button = "//button[text()='Swap']"
    zetalabs_notice = "//div[contains(@class,'MuiPaper-root MuiPaper-elevation')]"
    # 数据库表头
    taskName = 'Zetalabs'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)
        self.q = Query()
        self.qe = Query()
        self.q_swapTime = Query()

    # zetalabs网站领取测试币功能
    def zeta_getToken(self, adsNum):
        # 打开https://labs.zetachain.com/get-zeta页面
        self.driver.browser.navi_to_page(self.zetalabs_get_url)
        time.sleep(5)
        try:
            # 点击get-zeta按钮
            self.driver.element.click(self.zetalabs_get_button)
            try:
                # 测试币领好后获取try-swapping按钮
                self.driver.find.xpath_element_presence_60sec(self.zetalabs_try_swapping)
                self.q.add(self.taskName, self.zetalabs_getToken, adsNum)
            except BaseException:
                pass
            # 点击try-swapping按钮进行SWAP操作
            # self.zeta_swap(acd)
        except BaseException:
            # 定义测试币还有多久可以领取，并写入EXCEL
            next_time = self.driver.element.get_text(self.zetalabs_next_time)
            self.q.add(self.taskName, next_time, adsNum)

    def zeta_swap(self, adsNum):
        self.driver.browser.navi_to_page(self.zetalabs_swap_url)
        time.sleep(5)
        try:
            self.driver.element.click("//img[@alt='close']")
        except BaseException:
            pass
        # 配置SWAP兑换元素，并输入0.1的数量
        self.driver.element.click(self.zetalabs_swapNetwork)
        self.driver.mouse.many_TAB_ENTER(4)
        self.driver.element.click(self.zetalabs_swapToken)
        self.driver.mouse.many_TAB_ENTER(3)
        self.driver.element.click(self.zetalabs_receiveNetwork)
        self.driver.mouse.many_TAB_ENTER(3)
        self.driver.element.click(self.zetalabs_receiveToken)
        self.driver.mouse.many_TAB_ENTER(4)
        self.driver.element.send_keys(self.zetalabs_input, '2.6')
        time.sleep(5)
        review = self.driver.element.get_text(self.zetalabs_review_button)
        if review == 'Review Order':
            self.driver.element.click(self.zetalabs_review_button)
            time.sleep(3)
        else:
            self.driver.element.click(self.zetalabs_review_button)
            time.sleep(3)
            self.wallet.metamask_switch()
            self.driver.element.click(self.zetalabs_review_button)
            time.sleep(5)
        swap = self.driver.element.get_text(self.zetalabs_empower_button)
        print(swap)
        if swap == 'Swap':
            self.driver.element.click(self.zetalabs_swap_button)
            time.sleep(5)
        else:
            self.driver.element.click(self.zetalabs_empower_button)
            time.sleep(5)
            self.wallet.metamask_empower()
            # 判断swap按钮是否可点击，一直等待到swap按钮返回True（可点击）为止
            while True:
                swap = self.driver.find.xpath_enable(self.zetalabs_swap_button)
                if swap:
                    break
            self.driver.element.click(self.zetalabs_swap_button)
            time.sleep(5)
        self.wallet.metamask_submit()
        # 获取SWAP成功后的通知文本，并写入EXCEL
        notion = self.driver.element.get_text_60sec(self.zetalabs_notice)
        if 'again' in notion:
            self.qe.add(self.taskName, notion, adsNum)
        else:
            self.qe.add(self.taskName, self.zetalabs_success, adsNum)
            self.q_swapTime.add('ZetalabsTime', time.ctime(), adsNum)
