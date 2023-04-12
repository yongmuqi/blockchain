import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query


class Coingecko:
    coingecko_url = 'https://www.coingecko.com/account/candy?locale=zh'
    coingecko_button = "//button[contains(@class,'btn btn-primary')]"
    coingecko_msg = "//div[contains(@class,'col-8 col-lg-10')]//span"
    coingecko_nextTime = "//span[@data-target='points.nextDailyRewardCountdownTimer']"
    # 数据库表名
    taskName = 'CoinGecko'

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.q = Query()

    def coingecko_get(self, adsNum, tableName):
        # 打开领取糖果页面，并等待5秒
        self.driver.browser.navi_to_page(self.coingecko_url)
        time.sleep(5)
        try:
            self.driver.element.click_3sec("(//div[@class='tw-flex-1'])[2]")
        except BaseException:
            pass
        # 判断领取糖果的按钮是否可以点击，可点击：点击并刷新页面获取最近点击的时间
        try:
            button = self.driver.element.get_is_enabled(self.coingecko_button)
            if button:
                self.driver.element.click(self.coingecko_button)
                time.sleep(5)
                self.driver.browser.refresh()
                msg = self.driver.element.get_text(self.coingecko_msg)
                self.q.add(tableName, self.taskName, msg, adsNum)
        # 按钮不可点击，则代表今天已经点击过了，则获取下次领取的时间
        except BaseException:
            next_msg = '下次：' + self.driver.element.get_text(self.coingecko_nextTime)
            self.q.add(tableName, self.taskName, next_msg, adsNum)
