from .browser import Browser
from .element import Element
from .find import Find
from .mouse import Mouse
from .wait import Wait
from .alert import Alert
from .mysql import Query
from .config import Config


class actionsBase:
    driver = None

    # 封装初始化浏览器
    def __init__(self, driver):
        self.wait = Wait(driver)
        self.find = Find(driver)
        self.browser = Browser(driver)
        self.element = Element(driver)
        self.mouse = Mouse(driver)
        self.alert = Alert(driver)
        self.config = Config()
        self.mysql = Query()
