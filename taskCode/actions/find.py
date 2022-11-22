from selenium.webdriver.common.by import By

from taskCode.actions.wait import Wait


class Find:
    def __init__(self, driver):
        self.wait = Wait(driver)
        self.driver = driver

    # 没有封装的find_element
    def findX(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    # 封装定位元素xpath功能，等待10秒（元素可见）
    def xpath_element(self, xpath):
        return self.wait.wait_visibility_of_element(xpath)

    # 封装定位元素xpath功能，等待60秒（元素可见）
    def xpath_element_visibility_60sec(self, xpath):
        return self.wait.wait_visibility_of_element_60sec(xpath)

    # 封装等待元素消失功能，等待60秒
    def xpath_notElement_60sec(self, xpath):
        return self.wait.wait_visibility_of_notElement_60sec(xpath)

    # 封装定位元素xpath功能，等待10秒（不关心元素是否可见）
    def xpath_element_presence(self, xpath):
        return self.wait.wait_presence_of_element(xpath)

    # 封装定位元素xpath功能，等地60秒（不关心元素是否可见）
    def xpath_element_presence_60sec(self, xpath):
        return self.wait.wait_presence_of_element_60sec(xpath)

    # 封装等待页面元素出现判断元素是否可以点击，等待时间：10秒
    def xpath_enable(self, xpath):
        return self.wait.wait_element_to_be_clickable(xpath)

    # 封装定位元素xpath功能(CLASSNAME)
    def className_element(self, xpath):
        return self.wait.wait_visibility_of_element_CLASSNAME(xpath)
