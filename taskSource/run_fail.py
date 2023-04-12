import threading
import time

import requests
from taskSource.method.config import Config
from taskSource.task import Task
from taskSource.method.drivers import Drivers
from taskSource.method.bitDriver import bitDriver
from taskSource.method.mysql import Mysql


def adsFail():
    ads_CarvFail = Mysql().findDate('ads_task', 'Carv', '失败')
    ads_CKGFail = Mysql().findDate_3('ads_task', 'Coingecko', '天前', '小时前')
    ads_ZetaTokenFail = Mysql().findDate_3('ads_task', 'Zetalabs', 'You will receive', '失败')
    ads_CassFail = Mysql().findDate('ads_task', 'Cassava', '失败')
    ads_Layer3Fail = Mysql().findDate('ads_task', 'Layer3', '没有内容')
    ads_SoquestFail = Mysql().findDate('ads_task', 'Soquest', '没有内容')

    ads_CarvFailList = []
    ads_CKGFailList = []
    ads_ZetaTokenFailList = []
    ads_CassFailList = []
    ads_Layer3FailList = []
    ads_SoquestFailList = []

    for failNum in ads_CarvFail:
        ads_CarvFailList.append(int(failNum))

    for failNum in ads_CKGFail:
        ads_CKGFailList.append(int(failNum))

    for failNum in ads_ZetaTokenFail:
        ads_ZetaTokenFailList.append(int(failNum))

    for failNum in ads_CassFail:
        ads_CassFailList.append(int(failNum))

    for failNum in ads_Layer3Fail:
        ads_Layer3FailList.append(int(failNum))

    for failNum in ads_SoquestFail:
        if int(failNum) < 26:
            ads_SoquestFailList.append(int(failNum))

    return ads_CarvFailList, ads_CKGFailList, ads_ZetaTokenFailList, ads_CassFailList, ads_Layer3FailList, ads_SoquestFailList


def bitFail():
    bit_CarvFail = Mysql().findDate('bit_task', 'Carv', '失败')
    bit_CKGFail = Mysql().findDate_3('bit_task', 'Coingecko', '天前', '小时前')
    bit_ZetaTokenFail = Mysql().findDate_3('bit_task', 'Zetalabs', 'You will receive', '失败')
    bit_CassFail = Mysql().findDate('bit_task', 'Cassava', '失败')
    bit_Layer3Fail = Mysql().findDate('bit_task', 'Layer3', '没有内容')

    bit_CarvFailList = []
    bit_CKGFailList = []
    bit_ZetaTokenFailList = []
    bit_CassFailList = []
    bit_Layer3FailList = []

    for failNum in bit_CarvFail:
        bit_CarvFailList.append(int(failNum))

    for failNum in bit_CKGFail:
        bit_CKGFailList.append(int(failNum))

    for failNum in bit_ZetaTokenFail:
        bit_ZetaTokenFailList.append(int(failNum))

    for failNum in bit_CassFail:
        bit_CassFailList.append(int(failNum))

    for failNum in bit_Layer3Fail:
        bit_Layer3FailList.append(int(failNum))

    return bit_CarvFailList, bit_CKGFailList, bit_ZetaTokenFailList, bit_CassFailList, bit_Layer3FailList


class run_fail:
    def __init__(self):
        self.drivers = Drivers()

    def adsTask(self, Num, taskName):
        # 定义acc为账号id
        adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(Num)
        tableName = 'ads_task'
        url = "http://local.adspower.net:50325/api/v1/browser/"
        close_url = url + "stop?user_id=" + adsId
        align_mapping = {
            1: 'topLeft',
            2: 'topRight',
            3: 'bottomLeft',
            0: 'bottomRight',
        }
        align = align_mapping[Num % 4]
        ads_driver = self.drivers.drivers(adsId, tableName, align)

        ads = Task(ads_driver)

        if taskName == 'Zeta':
            try:
                ads.wallet.metaMask_Login(adsNum, tableName)
                ads.zetalabs.zetaTask(adsNum, tableName)
            except BaseException:
                pass

        if taskName == 'Carv':
            try:
                ads.wallet.metaMask_Login(adsNum, tableName)
                ads.carv.carvTask(adsNum, tableName)
            except BaseException:
                pass

        if taskName == 'Coingecko':
            try:
                ads.coingecko.coingeckoTask(adsNum, tableName)
            except BaseException:
                pass

        if taskName == 'Layer3':
            try:
                ads.layer3.layer3Task(adsNum, tableName)
            except BaseException:
                pass

        if taskName == 'Soquest':
            try:
                ads.wallet.metaMask_Login(adsNum, tableName)
                ads.coingecko.soquestTask(adsNum, tableName)
            except BaseException:
                pass

        if taskName == 'Cassava':
            try:
                ads.coingecko.cassavaTask(adsNum, tableName)
            except BaseException:
                pass

        ads_driver.close()
        ads_driver.quit()
        requests.get(close_url)

    def adsWork(self, Num, taskName):
        with sem:
            self.adsTask(Num, taskName)

    def bitTask(self, Num, taskName):
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
        bit_driver = self.drivers.drivers(bitId, tableName, align)

        bit = Task(bit_driver)
        # 执行任务
        if taskName == 'Carv':
            try:
                bit.wallet.metaMask_Login(bitNum, tableName)
                bit.carv.carvTask(bitNum, tableName)
            except BaseException:
                pass

        if taskName == 'Layer3':
            try:
                bit.layer3.layer3Task(bitNum, tableName)
            except BaseException:
                pass

        if taskName == 'Coingecko':
            try:
                bit.coingecko.coingeckoTask(bitNum, tableName)
            except BaseException:
                pass

        if taskName == 'Cassava':
            try:
                bit.coingecko.cassavaTask(bitNum, tableName)
            except BaseException:
                pass

        if taskName == 'Zeta':
            try:
                bit.wallet.metaMask_Login(bitNum, tableName)
                bit.zetalabs.zetaTask(bitNum, tableName)
            except BaseException:
                pass
        # 关闭浏览器
        bit_driver.close()
        bit_driver.close()
        self.drivers.bit_stopBrowser(bitId)

    def bitWork(self, Num, taskName):
        with sem:
            self.bitTask(Num, taskName)


if __name__ == "__main__":
    adsCarvFailList = adsFail()[0]
    adsCKGFailList = adsFail()[1]
    adsZetaTokenFailList = adsFail()[2]
    adsCassFailList = adsFail()[3]
    adsLayer3FailList = adsFail()[4]
    adsSoquestFailList = adsFail()[5]
    print("ADS_CARV失败列表：", adsCarvFailList)
    print("ADS_糖果失败列表：", adsCKGFailList)
    print("ADS_ZETA失败列表：", adsZetaTokenFailList)
    print("ADS_CASS失败列表：", adsCassFailList)
    print("ADS_LAYER3失败列表：", adsLayer3FailList)
    print("ADS_SOQUEST失败列表：", adsSoquestFailList)

    bitCarvFailList = bitFail()[0]
    bitCKGFailList = bitFail()[1]
    bitZetaTokenFailList = bitFail()[2]
    bitCassFailList = bitFail()[3]
    bitLayer3FailList = bitFail()[4]
    print("BIT_CARV失败列表：", bitCarvFailList)
    print("BIT_糖果失败列表：", bitCKGFailList)
    print("BIT_ZETA失败列表：", bitZetaTokenFailList)
    print("BIT_CASS失败列表：", bitCassFailList)
    print("BIT_LAYER3失败列表：", bitLayer3FailList)

    sem = threading.Semaphore(4)
    threadList = []
    for i in adsCarvFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().adsWork, args=(i, 'Carv',))
        threadList.append(thread)
        thread.start()
    for i in adsCKGFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().adsWork, args=(i, 'Coingecko',))
        threadList.append(thread)
        thread.start()
    for i in adsZetaTokenFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().adsWork, args=(i, 'Zeta',))
        threadList.append(thread)
        thread.start()
    for i in adsCassFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().adsWork, args=(i, 'Cassava',))
        threadList.append(thread)
        thread.start()
    for i in adsLayer3FailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().adsWork, args=(i, 'Layer3',))
        threadList.append(thread)
        thread.start()
    for i in adsSoquestFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().adsWork, args=(i, 'Soquest',))
        threadList.append(thread)
        thread.start()

    for i in bitCarvFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().bitWork, args=(i, 'Carv',))
        threadList.append(thread)
        thread.start()
    for i in bitCKGFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().bitWork, args=(i, 'Coingecko',))
        threadList.append(thread)
        thread.start()
    for i in bitZetaTokenFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().bitWork, args=(i, 'Zeta',))
        threadList.append(thread)
        thread.start()
    for i in bitCassFailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().bitWork, args=(i, 'Cassava',))
        threadList.append(thread)
        thread.start()
    for i in bitLayer3FailList:
        time.sleep(5)
        thread = threading.Thread(target=run_fail().bitWork, args=(i, 'Layer3',))
        threadList.append(thread)
        thread.start()