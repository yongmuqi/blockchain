import threading
import time
from actions.config import Config
from sourceCode import taskBase
from taskCode.actions.drivers import Drivers
from taskCode.actions.bitDriver import bitDriver


class run_all:
    def __init__(self):
        self.adsDriver = Drivers()
        self.bitDriver = bitDriver()

    def bitTask(self, Num):
        # 定义bitId为账号id
        bitId = Config.bitId(Num)
        # 定义bitNum为窗口编号
        bitNum = Config.bitNum(Num)
        # 定义bitAddress为钱包地址
        bitAddress = Config.bitAddress(Num)
        # 定义bitMail为邮箱地址
        bitMail = Config.bitMail(Num)
        # 定义bitName为用户名
        bitName = Config.bitName(Num)
        # 定义password为密码
        password = Config.password()
        # 初始化比特的浏览器
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

        bit = taskBase(driver)
        tableName = 'bit_task'
        # 执行任务
        try:
            bit.wallet.metamask_login(bitNum, tableName)
        except BaseException:
            pass
        # if Num <= 50:
        #     try:
        #         bit.carv.carv_checkin(bitNum, tableName)
        #     except BaseException:
        #         pass
        # if Num <= 50:
        try:
            bit.layer3.layer3(bitNum, tableName)
        except BaseException:
            pass
        # try:
        #     bit.coingecko.coingecko_get(bitNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     bit.layer3.cassava(bitNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     bit.zetalabs.zeta_getToken(bitNum, tableName)
        # except BaseException:
        #     pass
        # 关闭浏览器
        self.bitDriver.bit_stopBrowser(bitId)

    def bitWork(self, Num):
        with sem:
            self.bitTask(Num)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    all_bitNum = Config.all_bit()
    sem = threading.Semaphore(4)
    threadList = []
    list = [78,81]
    # for i in list:
    for i in range(52, len(all_bitNum) + 1):
        time.sleep(5)
        thread = threading.Thread(target=run_all().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()