import datetime
import threading
import time
import requests
from actions.config import Config
from sourceCode import taskBase
from taskCode.actions import Query
from taskCode.actions.drivers import Drivers
from taskCode.actions.bitDriver import bitDriver


def failList():
    ads_fusionistCheckFail = Query().findDate('ads_task', 'OtherTask1', '没有内容')
    ads_fusionistDrawFail = Query().findDate('ads_task', 'OtherTask2', '没有内容')
    bit_fusionistCheckFail = Query().findDate('bit_task', 'OtherTask1', '没有内容')
    bit_fusionistDrawFail = Query().findDate('bit_task', 'OtherTask2', '没有内容')
    ads2_fusionistCheckFail = Query().findDate_No('ads_task', 'OtherTask1', '二')
    ads2_fusionistDrawFail = Query().findDate_No('ads_task', 'OtherTask2', '二')
    bit2_fusionistCheckFail = Query().findDate_No('bit_task', 'OtherTask1', '二')
    bit2_fusionistDrawFail = Query().findDate_No('bit_task', 'OtherTask2', '二')

    ads_fusionistCheckList = []
    ads_fusionistDrawList = []
    bit_fusionistCheckList = []
    bit_fusionistDrawList = []

    nowTime = datetime.datetime.now()
    if nowTime.hour < 18:
        for failNum in ads_fusionistCheckFail:
            ads_fusionistCheckList.append(int(failNum))
        for failNum in ads_fusionistDrawFail:
            ads_fusionistDrawList.append(int(failNum))
        for failNum in bit_fusionistCheckFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistCheckList.append(int(failNum))
        for failNum in bit_fusionistDrawFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistDrawList.append(int(failNum))
    else:
        for failNum in ads2_fusionistCheckFail:
            ads_fusionistCheckList.append(int(failNum))
        for failNum in ads2_fusionistDrawFail:
            ads_fusionistDrawList.append(int(failNum))
        for failNum in bit2_fusionistCheckFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistCheckList.append(int(failNum))
        for failNum in bit2_fusionistDrawFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistDrawList.append(int(failNum))

    ads_fusionistCheckList.extend(ads_fusionistDrawList)
    ads_fusionistFail = []
    for ads_i in ads_fusionistCheckList:
        if ads_i not in ads_fusionistFail:
            ads_fusionistFail.append(ads_i)
    print(ads_fusionistFail)

    bit_fusionistCheckList.extend(bit_fusionistDrawList)
    bit_fusionistFail = []
    for bit_i in bit_fusionistCheckList:
        if bit_i not in bit_fusionistFail:
            bit_fusionistFail.append(bit_i)
    print(bit_fusionistFail)

    return ads_fusionistFail, bit_fusionistFail


class run_all:
    def __init__(self):
        self.adsDriver = Drivers()
        self.bitDriver = bitDriver()

    def adsTask(self, Num):
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
        ads.fusionist.fusionist(adsNum, tableName)

        adsDriver.close()
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
        if Num == 34:
            pass
        else:
            bit.fusionist.fusionist(bitNum, tableName)
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

    for i in range(1, len(all_adsNum) + 1):
        time.sleep(5)
        thread = threading.Thread(target=run_all().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()
    time.sleep(5)
    adsFusionistFail = failList()[0]
    for i in adsFusionistFail:
        time.sleep(5)
        thread = threading.Thread(target=run_all().adsWork, args=(i,))
        threadList.append(thread)
        thread.start()

    now = datetime.datetime.now()
    nowTIme = now.hour * 3600 + now.minute * 60 + now.second
    taskTime = 21 * 3600
    sleep = taskTime - nowTIme
    if sleep <= 0:
        time.sleep(sleep)
    else:
        print("等待时间：" + str(sleep) + "秒")
        time.sleep(1)
    for i in range(1, 65):
        time.sleep(5)
        thread = threading.Thread(target=run_all().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()
    time.sleep(5)
    bitFusionistFail = failList()[1]
    for i in bitFusionistFail:
        time.sleep(5)
        thread = threading.Thread(target=run_all().bitWork, args=(i,))
        threadList.append(thread)
        thread.start()