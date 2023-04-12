import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .element_Wait import Wait
from .element_Action import Element


class Function:
    def __init__(self, driver):
        self.driver = Wait(driver)
        self.element = Element(driver)

    # 通过CLASS_NAME在列表中寻找某个元素功能(用于metamask钱包切换网络用)
    def find_location(self, xpath, value):
        elements = self.driver.wait_visibility_of_elements_t(By.CLASS_NAME, xpath, 10)
        for element in elements:
            if value in element.text:
                element.click()
                break

    # 使用while等待某个按钮直到可以点击为止，并点击
    def wait_and_click_button(self, xpath, timeout=60):
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            button = self.element.get_button_enabled(xpath)
            if button:
                self.element.click(xpath)
                break
            elif elapsed_time > timeout:
                break
            time.sleep(1)

    # 等待文本发生变化
    def wait_for_text_change(self, xpath, timeout=60):
        initial_text = self.element.get_text(xpath)
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            current_text = self.element.get_text(xpath)
            if current_text != initial_text:
                break
            elif elapsed_time > timeout:
                break
            time.sleep(1)

    # 鼠标移动到(1,1)坐标并点击两次，防止有弹窗
    def offset_click_00(self):
        action = ActionChains(self.driver).move_by_offset(1, 1)
        action.click().perform()
        action.click().perform()
        action.reset_actions()
