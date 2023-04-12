import threading
import time
from method.config import Config
from taskSource.task import Task
from method.bitDriver import bitDriver


class All_Task:
    def __init__(self):
        self.bitDriver = bitDriver()

    def bitTask(self, Num):
        # 定义bitId为账号id
        bitId = Config.bitId(Num)
        # 定义bitNum为窗口编号
        bitNum = Config.bitNum(Num)
        bitAddress = Config.bitAddress(Num)
        # 设置奇数窗口在左，偶数窗口在右
        if Num in range(1, 100, 4):
            align = 'topLeft'
            driver = self.bitDriver.browser(bitId, align)
        elif Num in range(2, 100, 4):
            align = 'topRight'
            driver = self.bitDriver.browser(bitId, align)
        elif Num in range(3, 100, 4):
            align = 'bottomLeft'
            driver = self.bitDriver.browser(bitId, align)
        else:
            align = 'bottomRight'
            driver = self.bitDriver.browser(bitId, align)
        # align = 'right' if (Num % 2) == 0 else 'left'

        bit = Task(driver)
        tableName = 'bit_task'
        # 执行任务
        try:
            bit.wallet.metaMask_Login(bitNum, tableName)
        except BaseException:
            pass

        # try:
        #     bit.carv.carvTask(bitNum, tableName)
        # except BaseException:
        #     pass

        # try:
        #     bit.layer3.layer3Task(bitNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     bit.coingecko.coingeckoTask(bitNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     bit.coingecko.cassavaTask(bitNum, tableName)
        # except BaseException:
        #     pass

        # try:
        #     bit.zetalabs.zeta_swap(bitNum, tableName)
        # except BaseException:
        #     pass
        # bit.layer3.layer3Task(bitNum, tableName)
        # bit.scroll.scroll_zkSync_Task(bitNum)
        # bit.coingecko.cassavaTask(bitNum, tableName)

        # 关闭浏览器
        driver.close()
        driver.quit()
        self.bitDriver.bit_stopBrowser(bitId)

    def bitWork(self, Num):
        with sem:
            self.bitTask(Num)


if __name__ == "__main__":
    all_bitNum = Config.all_bit()
    sem = threading.Semaphore(4)
    threadList = []
    newList = [56,57,58,59,60,61,64,71,66,73,68,70]
    # for i in newList:
    for i in range(22, len(all_bitNum) + 1):
        time.sleep(5)
        thread = threading.Thread(target=All_Task().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()
