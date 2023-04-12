import time
from concurrent.futures import ThreadPoolExecutor
from blockchain.task import Task
from blockchain.method.config import Config
from blockchain.method.drivers import Drivers
from blockchain.method.mysql import Mysql


class All_Task:
    def __init__(self):
        self.driver = Drivers()

    def ads_task(self, Num):
        adsId = Config.adsId(Num)
        adsNum = Config.adsNum(Num)
        tableName = 'ads_task'
        # align = 'right' if (Num % 2) == 0 else 'left'
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

    def bit_task(self, Num):
        bitId = Config.bitId(Num)
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

        bit_driver.close()
        bit_driver.quit()


def worker(task_type, num):
    all_task = All_Task()
    if task_type == "ads":
        all_task.ads_task(num)
    elif task_type == "bit":
        all_task.bit_task(num)


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