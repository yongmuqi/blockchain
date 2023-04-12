import time
from taskCode.actions import actionsBase


class yesCaptcha:

    def __init__(self, driver):
        self.driver = actionsBase(driver)

    def openYesCaptcha(self):
        self.driver.browser.navi_to_page("chrome-extension://jiofmdifioeejeilfkpegipdjiopiekl/popup/index.html")
        time.sleep(2)
        try:
            statue = self.driver.find.xpath_element_3sec('//span[contains(@class, "Mui-checked css-1g3pnk5")]')
        except BaseException:
            self.driver.element.click('//*[@id="app"]/div/div[1]/div[2]/span/span[1]')

    def closeYesCaptcha(self):
        self.driver.browser.navi_to_page("chrome-extension://jiofmdifioeejeilfkpegipdjiopiekl/popup/index.html")
        time.sleep(2)
        try:
            statue = self.driver.find.xpath_element_3sec('//span[contains(@class, "Mui-checked css-1g3pnk5")]')
            self.driver.element.click('//*[@id="app"]/div/div[1]/div[2]/span/span[1]')
        except BaseException:
            pass