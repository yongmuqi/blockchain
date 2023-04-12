import time
from concurrent.futures import ThreadPoolExecutor
import requests
from method.config import Config
from taskSource.task import Task
from method.drivers import Drivers
from method.mysql import Mysql


class All_Task:
    def __init__(self):
        self.driver = Drivers()

    def adsTask(self, Num):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        tableName = 'ads_task'
        align_mapping = {
            1: 'topLeft',
            2: 'topRight',
            3: 'bottomLeft',
            0: 'bottomRight',
        }
        align = align_mapping[Num % 4]
        ads_driver = self.driver.drivers(adsId, tableName, align)
        ads = Task(ads_driver)
        try:
            ads.wallet.metaMask_Login(adsNum, tableName)
        except BaseException:
            pass

        try:
            ads.zetalabs.zetaTask(adsNum, tableName)
        except BaseException:
            pass

        try:
            ads.carv.carvTask(adsNum, tableName)
        except BaseException:
            pass

        try:
            ads.coingecko.coingeckoTask(adsNum, tableName)
        except BaseException:
            pass

        try:
            ads.layer3.layer3Task(adsNum, tableName)
        except BaseException:
            pass

        if Num < 26:
            try:
                ads.coingecko.soquestTask(adsNum, tableName)
            except BaseException:
                pass

        try:
            ads.coingecko.cassavaTask(adsNum, tableName)
        except BaseException:
            pass

        ads_driver.close()
        ads_driver.quit()
        requests.get(close_url)

    # def adsWork(self, Num):
    #     with sem:
    #         self.adsTask(Num)

    def bitTask(self, Num):
        # 定义bitId为账号id
        bitId = Config.bitId(Num)
        # 定义bitNum为窗口编号
        bitNum = Config.bitNum(Num)
        tableName = 'bit_task'
        # align = 'right' if (Num % 2) == 0 else 'left'
        align_mapping = {
            1: 'topLeft',
            2: 'topRight',
            3: 'bottomLeft',
            0: 'bottomRight',
        }
        align = align_mapping[Num % 4]
        bit_driver = self.driver.drivers(bitId, tableName, align)
        bit = Task(bit_driver)
        # 执行任务

        try:
            bit.wallet.metaMask_Login(bitNum, tableName)
        except BaseException:
            pass

        try:
            bit.carv.carvTask(bitNum, tableName)
        except BaseException:
            pass

        try:
            bit.layer3.layer3Task(bitNum, tableName)
        except BaseException:
            pass

        try:
            bit.coingecko.coingeckoTask(bitNum, tableName)
        except BaseException:
            pass

        try:
            bit.coingecko.cassavaTask(bitNum, tableName)
        except BaseException:
            pass

        try:
            bit.zetalabs.zetaTask(bitNum, tableName)
        except BaseException:
            pass
        # 关闭浏览器
        bit_driver.close()
        bit_driver.quit()
        Drivers().bit_stopBrowser(bitId)

    # def bitWork(self, Num):
    #     with sem:
    #         self.bitTask(Num)


def worker(task_type, num):
    all_task = All_Task()
    if task_type == "ads":
        all_task.adsTask(num)
    elif task_type == "bit":
        all_task.bitTask(num)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    all_bitNum = Config.all_bit()
    Mysql().creartDb_ads()
    Mysql().creartDb_bit()

    tasks = []

    for i in range(1, 51):
        tasks.append(("ads", i))

    for i in range(1, len(all_bitNum) + 1):
        tasks.append(("bit", i))

    with ThreadPoolExecutor(max_workers=4) as executor:
        for task in tasks:
            time.sleep(5)
            executor.submit(worker, *task)
    # all_adsNum = Config.all_ads()
    # all_bitNum = Config.all_bit()
    # sem = threading.Semaphore(4)
    # threadList = []
    # Mysql().creartDb_ads()
    # Mysql().creartDb_bit()
    # for i in range(1, 51):
    #     time.sleep(5)
    #     thread = threading.Thread(target=All_Task().adsWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()
    # time.sleep(5)
    # for i in range(1, len(all_bitNum)+1):
    #     time.sleep(5)
    #     thread = threading.Thread(target=All_Task().bitWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()
