import time

from selenium.webdriver import Keys

from taskSource.method import elementMethod
from taskSource.method.config_Wallet import Config_Wallet


class Discord:
    def __init__(self, driver):
        self.driver = elementMethod(driver)

    def answerQuestion(self, url, oneXpath, twoXpath, adsNum):
        # 打开DISCORD答题页面
        self.driver.element_Browser.navi_to_page(url)
        time.sleep(10)

        ans1 = self.driver.element_Wait.wait_visibility_of_element("//span[contains(text(),'Choose your answer here')]")
        # ans1_x = ans1.location.get('x')
        # ans1_y = ans1.location.get('y')
        self.driver.element_Action.click("//span[text()='Choose your answer here 👇']")
        time.sleep(3)
        self.driver.element_Action.click(oneXpath)
        time.sleep(5)
        notion = self.driver.element_Action.get_text_60sec("//*[text()='Your answer is: ']")
        print(adsNum + notion)

        ans2 = self.driver.element_Wait.wait_visibility_of_element("//span[text()='Choose your answer here 👇']")
        # ans2_x = ans2.location.get('x')
        # ans2_y = ans2.location.get('y')
        self.driver.element_Action.click("//span[text()='Choose your answer here 👇']")
        time.sleep(3)
        self.driver.element_Action.click(twoXpath)
        time.sleep(5)
        notion = self.driver.element_Action.get_text_60sec("//*[text()='Your answer is: ']")
        print(adsNum + notion)

    def suiFaucet(self, Num):
        suiWalletAddress = Config_Wallet.adsSui(Num)
        content = "!faucet " + suiWalletAddress
        self.driver.element_Browser.navi_to_page('https://discord.com/channels/916379725201563759/1037811694564560966')
        time.sleep(10)
        self.driver.element_Action.click('//div[@data-slate-node="element"]')
        time.sleep(1)
        self.driver.element_Action.send_keys('//div[@data-slate-node="element"]', content)
        time.sleep(1)
        self.driver.element_Mouse.keyboard_element(Keys.ENTER)
