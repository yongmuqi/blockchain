import threading
import time
import requests
from actions.config import Config
from task import taskBase
from taskCode.actions.drivers import Drivers


class run_all:
    def __init__(self):
        self.driver = Drivers()


    def taskDriver(self, Num):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        # 定义adsAddress为钱包地址
        adsAddress = Config.adsAddress(Num)
        # 定义password为密码
        password = Config.password()
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        # 设置奇数窗口在坐，偶数窗口在右
        if (Num % 2) == 0:
            align = 'right'
            driver = self.driver.Driver(adsId, align)
        else:
            align = 'left'
            driver = self.driver.Driver(adsId, align)

        tb = taskBase(driver)
        tb.wallet.metamask_login(adsNum)

        driver.quit()
        requests.get(close_url)

    def work(self, Num):
        with sem:
            self.taskDriver(Num)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    sem = threading.Semaphore(2)
    threadList = []
    for i in range(1, len(all_adsNum)+1):
        time.sleep(3)
        thread = threading.Thread(target=run_all().work, args=(i,))
        threadList.append(thread)
        thread.start()
