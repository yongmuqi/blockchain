import threading
import time

from sourceCode.method.config import Config
from sourceCode.method.wallet import Wallet
from sourceCode.method.drivers import Drivers
from sourceCode.task import Task


class run_All:
    def __init__(self, Num):
        self.adsId = Config.adsId(Num)
        self.adsNum = Config.adsNum(Num)
        self.bitId = Config.bitId(Num)
        self.bitNum = Config.bitNum(Num)

    def adsTask(self):
        tableName = 'ads_task'
        page, browser = Drivers().startBrowser(self.adsId, tableName)
        ads = Task(page, browser)

        Wallet(page, browser).metamask_login(self.adsNum, tableName)

        # ads.coinmarketcap.coinmarketcap_task(self.adsNum, tableName)

        page.close()
        browser.close()

    def adsWork(self):
        with sem:
            self.adsTask()

    def bitTask(self):
        tableName = 'bit_task'
        page, browser = Drivers().startBrowser(self.bitId, tableName)

        Wallet(page, browser).metamask_login(self.bitNum, tableName)

        page.close()
        browser.close()

    def bitWork(self):
        with sem:
            self.bitTask()


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    all_bitNum = Config.all_bit()
    sem = threading.Semaphore(1)
    threadList = []
    for i in range(48, 49):
        time.sleep(5)
        thread = threading.Thread(target=run_All(i).adsWork)
        threadList.append(thread)
        thread.start()
    # time.sleep(5)
    # for i in range(1, 2):
    #     time.sleep(5)
    #     thread = threading.Thread(target=run_All(i).bitWork)
    #     threadList.append(thread)
    #     thread.start()