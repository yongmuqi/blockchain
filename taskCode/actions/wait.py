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

    def wait_visibility_of_element_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until(EC.visibility_of_element_located(locator))
        return element

    def wait_visibility_of_element_CSS(self, xpath):
        locator = (By.CSS_SELECTOR, xpath)
        element = WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(locator))
        return element

    def wait_visibility_of_element_clickable_CSS(self, xpath):
        locator = (By.CSS_SELECTOR, xpath)
        element = WebDriverWait(self.driver, 20, 1).until(EC.element_to_be_clickable(locator))
        return element

    def wait_visibility_of_element_ID(self, xpath):
        locator = (By.ID, xpath)
        element = WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(locator))
        return element

    def wait_visibility_of_element_LINK_TEXT(self, xpath):
        locator = (By.LINK_TEXT, xpath)
        element = WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(locator))
        return element.click()

    def wait_visibility_of_elements_CSS(self, xpath):
        locator = (By.CSS_SELECTOR, xpath)
        element = WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_all_elements_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，且元素可见,等待时长：3秒
    def wait_visibility_of_element_3sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 3, 1).until(EC.visibility_of_element_located(locator))
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

    # 封装等待功能,找到全部页面元素是都存在页面上，不关心是否可见,等待时长：10秒
    def wait_presence_of_elements(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，不关心是否可见,等待时长：60秒
    def wait_presence_of_element_60sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located(locator))
        return element

    def wait_presence_of_notElement_60sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 60, 1).until_not(EC.presence_of_element_located(locator))
        return element

    # 等待页面元素出现判断元素是否可以点击,等待时长：10秒
    def wait_element_to_be_clickable(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(locator))
        return element

    # 等待页面弹窗出现并切入弹窗内
    def wait_alert_is_present(self):
        element = WebDriverWait(self.driver, 10, 1).until(EC.alert_is_present())
        return element

    # frame可见并切换到该frame上
    def wait_switch_to_frame(self, xpath):
        locator = (By.XPATH, xpath)
        WebDriverWait(self.driver, 10, 1).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def wait_switch_to_frame_CSS(self, xpath):
        locator = (By.CSS_SELECTOR, xpath)
        WebDriverWait(self.driver, 10, 1).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def wait_execute_script(self, js: str):
        self.driver.execute_script(js)

    def wait_execute_script_Down(self):
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

    # 切换到默认frame
    def wait_switch_to_default(self):
        self.driver.switch_to.default_content()

    # 切换到主界面
    def wait_switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 验证hCaptcha验证码自动执行成功（yescaptcha浏览器插件）
    def hCaptcha_successful(self, xpath):
        locator = (By.CSS_SELECTOR, '#anchor #checkbox')
        entry = self.driver.find_element(By.XPATH, xpath)
        self.driver.switch_to.frame(entry)
        while True:
            anchor = WebDriverWait(self.driver, 5, 1).until(EC.visibility_of_element_located(locator))
            time.sleep(5)
            checked = anchor.get_attribute('aria-checked')
            if str(checked) == 'true':
                break
        self.driver.switch_to.default_content()
        time.sleep(2)

    def reCaptcha_successful(self):
        timeTimes = 0
        self.wait_switch_to_default()
        self.wait_switch_to_frame_CSS('iframe[title="reCAPTCHA"]')
        while True:
            timeTimes = timeTimes + 6
            anchor = self.wait_visibility_of_element_ID('recaptcha-anchor')
            time.sleep(5)
            checked = anchor.get_attribute('aria-checked')
            if str(checked) == 'true':
                print("验证成功")
                break
            elif timeTimes > 60:
                break
        self.wait_switch_to_default()
        time.sleep(2)