from .element import Element
from .wait import Wait
from .mysql import Mysql
from .config import Config
from .browser import Browser
from .function import Function
from .mouse import Mouse


class Method:
    driver = None

    def __init__(self, driver):
        self.wait = Wait(driver)
        self.element = Element(driver)
        self.browser = Browser(driver)
        self.function = Function(driver)
        self.mouse = Mouse(driver)
        self.mysql = Mysql()
        self.config = Config()