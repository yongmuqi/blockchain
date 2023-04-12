import time

from taskCode.actions import actionsBase


class discord:
    def __init__(self, driver):
        self.driver = actionsBase(driver)

    def answerQuestion(self, url, oneXpath, twoXpath, adsNum):
        # 打开DISCORD答题页面
        self.driver.browser.navi_to_page(url)
        time.sleep(10)

        ans1 = self.driver.find.xpath_element("//span[contains(text(),'Choose your answer here')]")
        ans1_x = ans1.location.get('x')
        ans1_y = ans1.location.get('y')
        self.driver.element.click("//span[text()='Choose your answer here 👇']")
        time.sleep(3)
        self.driver.element.click(oneXpath)
        time.sleep(5)
        notion = self.driver.element.get_text_60sec("//*[text()='Your answer is: ']")
        print(adsNum + notion)

        ans2 = self.driver.find.xpath_element("//span[text()='Choose your answer here 👇']")
        ans2_x = ans2.location.get('x')
        ans2_y = ans2.location.get('y')
        self.driver.element.click("//span[text()='Choose your answer here 👇']")
        time.sleep(3)
        self.driver.element.click(twoXpath)
        time.sleep(5)
        notion = self.driver.element.get_text_60sec("//*[text()='Your answer is: ']")
        print(adsNum + notion)