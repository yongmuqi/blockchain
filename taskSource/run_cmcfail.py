import threading
import time
import requests
from method.config import Config
from taskSource.task import Task
from method.driver import Driver
from method.bitDriver import bitDriver
from taskSource.method import Mysql


def adsFail():
    ads_cmcFail = Mysql().findDate('ads_task', 'CoinMarketcap', '失败')
    ads_cmcFailList = []

    for failNum in ads_cmcFail:
        ads_cmcFailList.append(int(failNum))

    return ads_cmcFailList


def bitFail():
    bit_cmcFail = Mysql().findDate('bit_task', 'CoinMarketcap', '失败')
    bit_cmcFailList = []

    for failNum in bit_cmcFail:
        bit_cmcFailList.append(int(failNum))

    return bit_cmcFailList


class run_cmc:
    def __init__(self):
        self.adsDriver = Driver()
        self.bitDriver = bitDriver()

    def adsTask(self, Num):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        adsAddress = Config.adsAddress(Num)
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        adsDriver = self.adsDriver.Driver(adsId)

        ads = Task(adsDriver)
        tableName = 'ads_task'
        try:
            ads.coinmarketcap.CollectDiamonds(adsNum, tableName)
        except BaseException:
            pass

        adsDriver.close()
        adsDriver.quit()
        requests.get(close_url)

    def adsWork(self, Num):
        with sem:
            self.adsTask(Num)

    def bitTask(self, Num):
        # 定义bitId为账号id
        bitId = Config.bitId(Num)
        # 定义bitNum为窗口编号
        bitNum = Config.bitNum(Num)
        driver = self.bitDriver.browser(bitId)

        bit = Task(driver)
        tableName = 'bit_task'
        try:
            bit.coinmarketcap.CollectDiamonds(bitNum, tableName)
        except BaseException:
            pass
        # 关闭浏览器
        driver.close()
        driver.quit()
        self.bitDriver.bit_stopBrowser(bitId)

    def bitWork(self, Num):
        with sem:
            self.bitTask(Num)


if __name__ == "__main__":
    sem = threading.Semaphore(1)
    threadList = []
    adscmcFailList = adsFail()
    print("ADS_CMC失败列表：", adscmcFailList)
    for i in adscmcFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_cmc().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()
    time.sleep(3)
    bitcmcFailList = bitFail()
    print("BIT_CMC失败列表：", bitcmcFailList)
    for i in bitcmcFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_cmc().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()