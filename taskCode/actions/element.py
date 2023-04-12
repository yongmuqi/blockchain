import time
from .find import Find


class Element:
    def __init__(self, driver):
        self.find = Find(driver)
        self.driver = driver

    # 元素点击功能
    def click(self, xpath):
        self.find.xpath_element(xpath).click()

    # 元素点击功能,3秒
    def click_3sec(self, xpath):
        self.find.xpath_element_3sec(xpath).click()

    # 输入关键字
    def send_keys(self, xpath, value):
        self.find.xpath_element(xpath).send_keys(value)

    # 输入关键字
    def send_keys_3sec(self, xpath, value):
        self.find.xpath_element_3sec(xpath).send_keys(value)

    # 清楚输入框数据
    def clear(self, xpath):
        self.find.xpath_element(xpath).clear()

    # 获取元素文本信息，时长：10秒
    def get_text(self, xpath) -> str:
        return self.find.xpath_element(xpath).text

    # 获取元素文本信息，时长：60秒
    def get_text_60sec(self, xpath) -> str:
        return self.find.xpath_element_presence_60sec(xpath).text

    def get_text_t(self, by, xpath, t) -> str:
        return self.find.xpath_element_t(by, xpath, t).text

    # 获取页面元素是否可点击
    def get_is_enabled(self, xpath) -> bool:
        return self.find.xpath_element(xpath).is_enabled()

    def get_is_enabled_60sec(self, xpath) -> bool:
        return self.find.xpath_element_visibility_60sec(xpath).is_enabled()

    # 获取元素页面元素是否可见
    def get_is_displayed(self, xpath):
        return self.find.xpath_element_presence(xpath).is_displayed()

    # 获取元素页面是否已被选中
    def get_is_selected(self, xpath):
        return self.find.xpath_element_presence(xpath).is_selected()

    # 通过CLASS_NAME在列表中寻找某个元素功能(用于metamask钱包切换网络用)
    def find_location(self, name, value):
        ls = self.find.className_element(name)
        x = 0
        for location in ls:
            if value in location.text:
                ls[x].click()
                break
            x = x + 1

    # 使用while等待某个按钮直到可以点击为止，并点击
    def while_button_60sec(self, xpath):
        timeTimes = 0
        while True:
            timeTimes = timeTimes + 1
            time.sleep(1)
            button = self.get_is_enabled_60sec(xpath)
            if button:
                self.click(xpath)
                break
            elif timeTimes > 60:
                break

    def textChanel(self, xpath):
        text = self.get_text(xpath)
        timeTimes = 0
        while True:
            text1 = self.get_text(xpath)
            timeTimes = timeTimes + 1
            time.sleep(1)
            if text1 != text:
                break
            elif timeTimes > 60:
                break