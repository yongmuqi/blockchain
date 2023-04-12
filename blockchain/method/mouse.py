from .wait import Wait
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Mouse:

    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)

    # 鼠标移动到某个元素功能
    def move_on_element(self, xpath):
        element = self.wait.wait_visibility_of_element(xpath)
        ActionChains(self.driver).move_to_element(element).perform()

    # 鼠标移动到某个元素并点击
    def move_on_element_click(self, xpath):
        element = self.wait.wait_visibility_of_element(xpath)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # 鼠标双击功能
    def double_click(self, xpath):
        element = self.wait.wait_visibility_of_element(xpath)
        ActionChains(self.driver).double_click(element).perform()

    # 鼠标右键点击功能
    def right_click(self, xpath):
        element = self.wait.wait_visibility_of_element(xpath)
        ActionChains(self.driver).context_click(element).perform()

    # 鼠标移动到某个坐标点击功能
    def offset_click(self, x, y):
        action = ActionChains(self.driver).move_by_offset(x, y)
        action.click().perform()
        action.reset_actions()

    def click_hold_on(self, xpath):
        button = self.wait.wait_visibility_of_element(xpath)
        ActionChains(self.driver).click_and_hold(button).perform()

    # 键盘按钮点击功能
    def keyboard_element(self, value):
        element = ActionChains(self.driver)
        element.send_keys(value).perform()

    # ctrl+v功能
    def ctrl_v(self):
        element = ActionChains(self.driver)
        element.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    # ctrl+a全选功能 + 删除键
    def ctrl_a(self):
        element = ActionChains(self.driver)
        element.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        element.send_keys(Keys.BACKSPACE).perform()
