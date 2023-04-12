import threading
import time
import requests
from method.config import Config
from taskSource.task import Task
from method.drivers import Drivers
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
        self.drivers = Drivers()

    def adsTask(self, Num):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        adsAddress = Config.adsAddress(Num)
        tableName = 'ads_task'
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        adsDriver = self.drivers.drivers(adsId, tableName)

        ads = Task(adsDriver)
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
        tableName = 'bit_task'
        driver = self.drivers.drivers(bitId, tableName)

        bit = Task(driver)
        try:
            bit.coinmarketcap.CollectDiamonds(bitNum, tableName)
        except BaseException:
            pass
        # 关闭浏览器
        driver.close()
        driver.quit()
        self.drivers.bit_stopBrowser(bitId)

    def bitWork(self, Num):
        with sem:
            self.bitTask(Num)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    all_bitNum = Config.all_bit()
    sem = threading.Semaphore(1)
    threadList = []
    for i in range(1, 51):
        time.sleep(5)
        thread = threading.Thread(target=run_cmc().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()
    time.sleep(3)
    for i in range(1, len(all_bitNum)+1):
        time.sleep(5)
        thread = threading.Thread(target=run_cmc().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()
    time.sleep(3)