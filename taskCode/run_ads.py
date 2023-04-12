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
        tableName = 'ads_task'
        # try:
        ads.wallet.metamask_login(adsNum, tableName)
        # except BaseException:
        #     pass
        time.sleep(10)

        # try:
        #     ads.carv.carv_checkin(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     ads.coingecko.coingecko_get(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     ads.layer3.layer3(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # try:
        #     ads.zetalabs.zeta_getToken(adsNum, tableName)
        # except BaseException:
        #     pass
        #
        # if Num < 9:
        #     try:
        #         ads.layer3.soquest(adsNum, tableName)
        #     except BaseException:
        #         pass
        #
        # try:
        #     ads.layer3.cassava(adsNum, tableName)
        # except BaseException:
        #     pass

        adsDriver.quit()
        requests.get(close_url)

    def adsWork(self, Num):
        with sem:
            self.adsTask(Num)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    sem = threading.Semaphore(4)
    threadList = []
    list = [1]
    for i in list:
    # for i in range(1, len(all_adsNum) + 1):
        time.sleep(5)
        thread = threading.Thread(target=run_all().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()
