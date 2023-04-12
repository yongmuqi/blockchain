import datetime
import os
import threading
import time
import requests
from actions.config import Config
from sourceCode import taskBase
from taskCode.actions.drivers import Drivers
from taskCode.actions.bitDriver import bitDriver
from taskCode.run_fusionist import failList


class run_all:
    def __init__(self):
        self.adsDriver = Drivers()
        self.bitDriver = bitDriver()


    def adsTask(self, Num, taskName):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
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

        ads = taskBase(adsDriver)
        tableName = 'ads_task'
        if taskName == 'ACE':
            try:
                ads.fusionist.fusionist(adsNum, tableName)
            except BaseException:
                pass

        elif taskName == 'ALL':
            try:
                ads.wallet.metamask_login(adsNum, tableName)
            except BaseException:
                pass

            try:
                ads.zetalabs.zeta_getToken(adsNum, tableName)
            except BaseException:
                pass

            try:
                ads.carv.carv_checkin(adsNum, tableName)
            except BaseException:
                pass

            try:
                ads.coingecko.coingecko_get(adsNum, tableName)
            except BaseException:
                pass

            try:
                ads.layer3.layer3(adsNum, tableName)
            except BaseException:
                pass


            if Num < 26:
                try:
                    ads.layer3.soquest(adsNum, tableName)
                except BaseException:
                    pass

            try:
                ads.layer3.cassava(adsNum, tableName)
            except BaseException:
                pass

        adsDriver.close()
        adsDriver.quit()
        requests.get(close_url)

    def adsWork(self, Num):
        with sem:
            self.adsTask(Num, 'ALL')

    def aceWork(self, Num):
        with sem:
            self.adsTask(Num, 'ACE')

    def bitTask(self, Num, taskName):
        # 定义bitId为账号id
        bitId = Config.bitId(Num)
        # 定义bitNum为窗口编号
        bitNum = Config.bitNum(Num)
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
        if taskName == 'ACE':
            if Num != 34:
                try:
                    bit.fusionist.fusionist(bitNum, tableName)
                except BaseException:
                    pass

        elif taskName == 'ALL':
            try:
                bit.wallet.metamask_login(bitNum, tableName)
            except BaseException:
                pass

            try:
                bit.carv.carv_checkin(bitNum, tableName)
            except BaseException:
                pass

            try:
                bit.layer3.layer3(bitNum, tableName)
            except BaseException:
                pass

            try:
                bit.coingecko.coingecko_get(bitNum, tableName)
            except BaseException:
                pass

            try:
                bit.layer3.cassava(bitNum, tableName)
            except BaseException:
                pass

            try:
                bit.zetalabs.zeta_getToken(bitNum, tableName)
            except BaseException:
                pass
        # 关闭浏览器
        self.bitDriver.bit_stopBrowser(bitId)

    def bitWork(self, Num):
        with sem:
            self.bitTask(Num, 'ALL')

    def aceBitWork(self, Num):
        with sem:
            self.bitTask(Num, 'ACE')


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    all_bitNum = Config.all_bit()
    adsFusionistFail = failList()[0]
    bitFusionistFail = failList()[1]
    sem = threading.Semaphore(4)
    threadList = []
    # for i in range(1, len(all_adsNum)+1):
    #     time.sleep(5)
    #     thread = threading.Thread(target=run_all().aceWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()
    # time.sleep(5)
    # for i in adsFusionistFail:
    #     time.sleep(5)
    #     thread = threading.Thread(target=run_all().aceWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()
    #
    #
    # now = datetime.datetime.now()
    # nowTIme = now.hour * 3600 + now.minute * 60 + now.second
    # taskTime = 9 * 3600
    # sleep = taskTime - nowTIme
    # if sleep <= 0:
    #     time.sleep(1)
    # else:
    #     time.sleep(sleep)
    # for i in range(14, 66):
    #     time.sleep(5)
    #     thread = threading.Thread(target=run_all().aceBitWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()
    # time.sleep(5)
    # for i in bitFusionistFail:
    #     time.sleep(5)
    #     thread = threading.Thread(target=run_all().bitWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()
    #
    # for i in range(1, len(all_adsNum)+1):
    #     time.sleep(5)
    #     thread = threading.Thread(target=run_all().adsWork, args=(i,))
    #     threadList.append(thread)
    #     thread.start()

    for i in range(1, len(all_bitNum) + 1):
        time.sleep(5)
        thread = threading.Thread(target=run_all().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()