import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Wait:
    def __init__(self, driver):
        self.driver = driver

    # 封装等待功能,找到页面元素是都存在页面上，且元素可见,等待时长：10秒
    def wait_visibility_of_element(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，且元素可见, 传入By和xpath，自定义时间
    def wait_visibility_of_element_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until(EC.visibility_of_element_located(locator))
        return element

    # 封装查找全部元素个能,等待时长：10秒
    def wait_visibility_of_elements(self, xpath):
        locator = (By.CSS_SELECTOR, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_all_elements_located(locator))
        return element

    # 封装查找全部元素个能, 传入By和xpath，自定义时间
    def wait_visibility_of_elements_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until(EC.visibility_of_all_elements_located(locator))
        return element

    # 判断元素按钮是否可以点击，返回True或Fail
    def wait_visibility_of_element_clickable(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(locator))
        return element

    # 判断元素按钮是否可以点击，返回True或Fail. 传入By和xpath，自定义时间
    def wait_visibility_of_element_clickable_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until(EC.element_to_be_clickable(locator))
        return element

    # 一直等待某个元素消失，默认超时60秒
    def wait_visibility_of_notElement_60sec(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 60, 1).until_not(EC.visibility_of_element_located(locator))
        return element

    # 一直等待某个元素消失，默认超时60秒. 传入By和xpath，自定义时间
    def wait_visibility_of_notElement_60sec_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until_not(EC.visibility_of_element_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，不关心是否可见,等待时长：10秒
    def wait_presence_of_element(self, xpath):
        locator = (By.XPATH, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(locator))
        return element

    # 封装等待功能,找到页面元素是都存在页面上，不关心是否可见, 传入By和xpath，自定义时间
    def wait_presence_of_element_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until(EC.presence_of_element_located(locator))
        return element

    # 封装查找全部元素功能,不关心元素是否可见等待时长：10秒
    def wait_presence_of_elements(self, xpath):
        locator = (By.CSS_SELECTOR, xpath)
        element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located(locator))
        return element

    # 封装查找全部元素功能,不关心是否可见。 传入By和xpath，自定义时间
    def wait_presence_of_elements_t(self, by, xpath, t):
        locator = (by, xpath)
        element = WebDriverWait(self.driver, t, 1).until(EC.presence_of_all_elements_located(locator))
        return element

    # 等待页面弹窗出现并切入弹窗内
    def wait_alert_is_present(self):
        element = WebDriverWait(self.driver, 10, 1).until(EC.alert_is_present())
        return element

    # 切换到默认frame
    def wait_switch_to_default(self):
        self.driver.switch_to.default_content()

    # 切换到主界面
    def wait_switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # frame可见并切换到该frame上
    def wait_switch_to_frame(self, xpath):
        locator = (By.XPATH, xpath)
        WebDriverWait(self.driver, 10, 1).until(EC.frame_to_be_available_and_switch_to_it(locator))

    # frame可见并切换到该frame上. 传入By和XPATH, 自定义时间
    def wait_switch_to_frame_t(self, by, xpath, t):
        locator = (by, xpath)
        WebDriverWait(self.driver, t, 1).until(EC.frame_to_be_available_and_switch_to_it(locator))

    # 执行JS脚本
    def wait_execute_script(self, js: str):
        self.driver.execute_script(js)

    # 执行JS脚本-滑动到页面底部
    def wait_execute_script_Down(self):
        js = f"document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

    def windows_zoom(self):
        script = f"document.body.style.zoom='50%'"
        self.driver.execute_script(script)

    def reCaptcha_successful(self):
        timeTimes = 0
        self.wait_switch_to_default()
        self.wait_switch_to_frame_t(By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]', 10)
        while True:
            timeTimes = timeTimes + 6
            anchor = self.wait_visibility_of_element_t(By.ID, 'recaptcha-anchor', 5)
            time.sleep(5)
            checked = anchor.get_attribute('aria-checked')
            if str(checked) == 'true':
                print("验证成功")
                break
            elif timeTimes > 60:
                break
        self.wait_switch_to_default()
        time.sleep(2)
