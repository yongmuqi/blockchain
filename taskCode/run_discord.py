import threading
import time
import requests
from actions.config import Config
from sourceCode import taskBase
from taskCode.actions.drivers import Drivers
from taskCode.actions.bitDriver import bitDriver

discordUrl = 'https://discord.com/channels/915445727600205844/972025568092647454/1063095422551334953'


class run_all:
    def __init__(self):
        self.adsDriver = Drivers()
        self.bitDriver = bitDriver()

    def adsTask(self, Num):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        # 定义adsAddress为钱包地址
        adsAddress = Config.adsAddress(Num)
        adsMail = Config.adsMail(Num)
        # 定义password为密码
        password = Config.password()
        adsDiscord = Config.adsDiscord(Num)
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        # 设置奇数窗口在左，偶数窗口在右
        if Num in range(1, 100, 4):
            align = 'topLeft'
            adsDriver = self.adsDriver.Driver(adsId, align)
        elif Num in range(2, 100, 4):
            align = 'topRight'
            adsDriver = self.adsDriver.Driver(adsId, align)
        elif Num in range(3, 100, 4):
            align = 'bottomLeft'
            adsDriver = self.adsDriver.Driver(adsId, align)
        else:
            align = 'bottomRight'
            adsDriver = self.adsDriver.Driver(adsId, align)
        # if (Num % 2) == 0:
        #     align = 'right'
        #     adsDriver = self.adsDriver.Driver(adsId, align)
        # else:
        #     align = 'left'
        #     adsDriver = self.adsDriver.Driver(adsId, align)

        ads = taskBase(adsDriver)
        oneXpath = '//img[@alt="1️⃣"]'
        twoXpath = '//img[@alt="2️⃣"]'
        threeXpath = '//img[@alt="3️⃣"]'
        fourXpath = '//img[@alt="4️⃣"]'
        try:
            ads.discords.answerQuestion(discordUrl, oneXpath, twoXpath, adsNum)
        except BaseException:
            pass

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
        # 执行任务
        oneXpath = '//img[@alt="1️⃣"]'
        twoXpath = '//img[@alt="2️⃣"]'
        threeXpath = '//img[@alt="3️⃣"]'
        fourXpath = '//img[@alt="4️⃣"]'
        try:
            bit.discords.answerQuestion(discordUrl, oneXpath, twoXpath, bitNum)
        except BaseException:
            pass
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
    list = [3]
    # for i in list:
    for i in range(1, len(all_adsNum) + 1):
        time.sleep(5)
        thread = threading.Thread(target=run_all().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()
    for i in range(1, 31):
        time.sleep(5)
        thread = threading.Thread(target=run_all().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()
