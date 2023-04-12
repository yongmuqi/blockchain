from .element_Wait import Wait
from .element_Browser import Browser
from .element_Alert import Alert
from .element_Action import Element
from .element_Mouse import Mouse
from .element_Function import Function
from .mysql import Mysql
from .config import Config


class elementMethod:
    driver = None

    def __init__(self, driver):
        self.element_Wait = Wait(driver)
        self.element_Browser = Browser(driver)
        self.element_Action = Element(driver)
        self.element_Mouse = Mouse(driver)
        self.element_Alert = Alert(driver)
        self.element_Function = Function(driver)
        self.mysql = Mysql()
        self.config = Config()
