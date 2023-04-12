import threading
import time
import requests
from method.config import Config
from taskSource.task import Task
from method.drivers import Drivers


class All_Task:
    def __init__(self):
        self.adsDriver = Drivers()

    def adsTask(self, Num):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        adsAddress = Config.bitAddress(Num)
        tableName = 'ads_task'
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        # 设置奇数窗口在左，偶数窗口在右
        # if Num in range(1, 100, 4):
        #     align = 'topLeft'
        #     adsDriver = self.adsDriver.Driver(adsId, align)
        # elif Num in range(2, 100, 4):
        #     align = 'topRight'
        #     adsDriver = self.adsDriver.Driver(adsId, align)
        # elif Num in range(3, 100, 4):
        #     align = 'bottomLeft'
        #     adsDriver = self.adsDriver.Driver(adsId, align)
        # else:
        #     align = 'bottomRight'
        #     adsDriver = self.adsDriver.Driver(adsId, align)
        # 设置奇数窗口在左，偶数窗口在右
        align = 'right' if (Num % 2) == 0 else 'left'

        adsDriver = self.adsDriver.drivers(adsId, tableName, align)
        ads = Task(adsDriver)
        # try:
        ads.wallet.metaMask_Login(adsNum, tableName)
        # except BaseException:
        #     pass

        # try:
        #     ads.zetalabs.zeta_swap(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     ads.carv.carvTask(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     ads.coingecko.coingeckoTask(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     ads.layer3.layer3Task(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # if Num < 26:
        #     try:
        #         ads.coingecko.soquestTask(adsNum, tableName)
        #     except BaseException:
        #         pass
        #
        # try:
        #     ads.coingecko.cassavaTask(adsNum, tablself.bitDriver.bit_stopBrowser(bitId)eName)
        # except BaseException:
        #     pass

        # try:
        #     ads.coinmarketcap.CollectDiamonds(adsNum, tableName)
        # except BaseException:
        #     pass

        # ads.scroll.scroll_zkSync_Task(adsNum)
        # ads.coingecko.CyberConnect(adsNum)
        ads.carv.carvTask(adsNum, tableName)
        adsDriver.close()
        adsDriver.quit()
        requests.get(close_url)

    def adsWork(self, Num):
        with sem:
            self.adsTask(Num)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    sem = threading.Semaphore(2)
    threadList = []
    newList = [7,8,9,10,11,13,14,15,16,17,18,19,20]
    # for i in newList:
    for i in range(3, 4):
        time.sleep(5)
        thread = threading.Thread(target=All_Task().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()
