import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Wait:
    def __init__(self, driver):
        self.driver = driver

    # 封装等待功能,找到页面元素是都存在页面上，且元素可见,等待时长：10秒
    def wait_visibility_of_element(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(locator))
        return element

    # 通过CLASS_NAME封装等待功能,找到页面元素是都存在页面上，且元素可见,等待时长：10秒
    def wait_visibility_of_element_CLASSNAME(self, xpath):
        locator = (By.CLASS_NAME, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_all_elements_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，且元素可见,等待时长：60秒
    def wait_visibility_of_element_60sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located(locator))
        return element

    # 一直等待某个元素消失，默认超时120秒
    def wait_visibility_of_notElement_60sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 120, 1).until_not(EC.visibility_of_element_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，不关心是否可见,等待时长：10秒
    def wait_presence_of_element(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，不关心是否可见,等待时长：60秒
    def wait_presence_of_element_60sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located(locator))
        return element

    # 等待页面元素出现判断元素是否可以点击,等待时长：10秒
    def wait_element_to_be_clickable(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 30, 1).until(EC.element_to_be_clickable(locator))
        return element

    # 等待页面弹窗出现并切入弹窗内
    def wait_alert_is_present(self):
        element = WebDriverWait(self.driver, 10, 1).until(EC.alert_is_present())
        return element

    # frame可见并切换到该frame上
    def wait_switch_to_frame(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.frame_to_be_available_and_switch_to_it(locator))
        return element

    def hCaptcha_successful(self):
        locator = (By.CSS_SELECTOR, '#anchor #checkbox')
        entry = self.driver.find_element(By.XPATH, '//*[@id="captcha-1"]/div/iframe')
        self.driver.switch_to.frame(entry)
        while True:
            anchor = WebDriverWait(self.driver, 5, 1).until(EC.visibility_of_element_located(locator))
            time.sleep(5)
            checked = anchor.get_attribute('aria-checked')
            if str(checked) == 'true':
                print(checked)
                break
        self.driver.switch_to.default_content()
        time.sleep(2)