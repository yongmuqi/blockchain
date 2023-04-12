from .element_Wait import Wait


class Alert:
    def __init__(self, driver):
        self.driver = Wait(driver)

    # 接受alert弹窗
    def accept_alert(self):
        self.driver.wait_alert_is_present().accpet()

    # 取消alert弹窗
    def dismiss_alert(self):
        self.driver.wait_alert_is_present().dismiss()

    # alert弹窗中输入字段
    def input_alert(self, value):
        self.driver.wait_alert_is_present().send_keys(value)

    # 获取alert弹窗显示字段
    def get_alert_text(self) -> str:
        return self.driver.wait_alert_is_present().text