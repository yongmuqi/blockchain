from taskCode.actions.find import Find
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Mouse:

    def __init__(self, driver):
        self.find = Find(driver)
        self.driver = driver

    # 鼠标移动到某个元素功能
    def move_on_element(self, xpath):
        element = self.find.xpath_element(xpath)
        ActionChains(self.driver).move_to_element(element).perform()

    # 鼠标移动到某个元素并点击
    def move_on_element_click(self, xpath):
        element = self.find.xpath_element(xpath)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # 鼠标双击功能
    def double_click(self, xpath):
        element = self.find.xpath_element(xpath)
        ActionChains(self.driver).double_click(element).perform()

    # 鼠标右键点击功能
    def right_click(self, xpath):
        element = self.find.xpath_element(xpath)
        ActionChains(self.driver).context_click(element).perform()

    # 鼠标移动到某个坐标点击功能
    def offset_click(self, x, y):
        action = ActionChains(self.driver).move_by_offset(x, y)
        action.click().perform()
        action.reset_actions()

    # 键盘按钮点击功能
    def keyboard_element(self, value):
        element = ActionChains(self.driver)
        element.send_keys(value).perform()

    # zetalabs&coinmarketcap TAB键2次，ENTER键1次功能
    def zetalabs_keyboard(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB).perform()
        action.send_keys(Keys.ENTER).perform()

    # 循环点击TAB键后按ENTER键
    def many_TAB_ENTER(self, i):
        action = ActionChains(self.driver)
        for x in range(i):
            action.send_keys(Keys.TAB).perform()
        action.send_keys(Keys.ENTER).perform()
