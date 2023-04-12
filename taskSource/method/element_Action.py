from .element_Wait import Wait


class Element:
    def __init__(self, driver):
        self.driver = Wait(driver)

    # 元素点击功能
    def click(self, xpath):
        self.driver.wait_visibility_of_element(xpath).click()

    # 元素点击， 自定义功能
    def click_t(self, by, xpath, t):
        self.driver.wait_visibility_of_element_t(by, xpath, t).click()

    def send_keys(self, xpath, value):
        self.driver.wait_visibility_of_element(xpath).send_keys(value)

    def send_keys_t(self, by, xpath, value, t):
        self.driver.wait_visibility_of_element_t(by, xpath, t).send_keys(value)

    def clear(self, xpath):
        self.driver.wait_visibility_of_element(xpath).clear()

    def get_text(self, xpath):
        return self.driver.wait_presence_of_element(xpath).text

    def get_text_t(self, by, xpath, t):
        return self.driver.wait_presence_of_element_t(by, xpath, t).text

    def get_button_enabled(self, xpath):
        return self.driver.wait_visibility_of_element(xpath).is_enabled()

    def get_button_enabled_t(self, by, xpath, t):
        return self.driver.wait_visibility_of_element_t(by, xpath, t).is_enabled()

    def get_is_displayed(self, xpath):
        element = self.driver.wait_visibility_of_element(xpath)
        return element.is_displayed()

    def get_is_selected(self, xpath):
        element = self.driver.wait_visibility_of_element(xpath)
        return element.is_selected()