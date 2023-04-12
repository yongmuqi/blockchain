import requests

from taskSource.method import Config
from taskSource.method.driver import Driver
from taskSource.task import Task
from taskSource.method.bitDriver import bitDriver


class run_views:

    @staticmethod
    def adsTask(inputNum, checkboxNum):
        for x in inputNum:
            # 定义acc为账号id
            adsId = Config.adsId(x)
            # 定义adsNUm为窗口编号
            adsNum = Config.adsNum(x)
            url = "http://local.adspower.net:50325/api/v1/browser/"
            open_url = url + "start?user_id=" + adsId + "&open_tabs=1"
            close_url = url + "stop?user_id=" + adsId
            driver = Driver().Driver(adsId)
            tb = Task(driver)
            tableName = 'ads_task'

            if 1 in checkboxNum:
                # try:
                tb.wallet.metaMask_Login(adsNum, tableName)
                tb.carv.carvTask(adsNum, tableName)
                # except BaseException:
                #     pass

            if 2 in checkboxNum:
                try:
                    tb.wallet.metaMask_Login(adsNum, tableName)
                    tb.layer3.layer3Task(adsNum, tableName)
                except BaseException:
                    pass

            if 3 in checkboxNum:
                try:
                    tb.coingecko.coingeckoTask(adsNum, tableName)
                except BaseException:
                    pass

            if 4 in checkboxNum:
                try:
                    tb.wallet.metaMask_Login(adsNum, tableName)
                    tb.zetalabs.zetaTask(adsNum, tableName)
                except BaseException:
                    pass

            if 5 in checkboxNum:
                try:
                    tb.coingecko.cassavaTask(adsNum, tableName)
                except BaseException:
                    pass

            if 6 in checkboxNum:
                try:
                    tb.wallet.metaMask_Login(adsNum, tableName)
                    tb.coingecko.soquestTask(adsNum, tableName)
                except BaseException:
                    pass

            if 7 in checkboxNum:
                try:
                    tb.coinmarketcap.CollectDiamonds(adsNum, tableName)
                except BaseException:
                    pass

            driver.close()
            driver.quit()
            requests.get(close_url)

    @staticmethod
    def bitTask(inputNum, checkboxNum):
        for x in inputNum:
            # 定义bitId为账号id
            bitId = Config.bitId(x)
            # 定义bitNum为窗口编号
            bitNum = Config.bitNum(x)

            driver = bitDriver().browser(bitId)
            tb = Task(driver)
            tableName = 'bit_task'

            if 1 in checkboxNum:
                try:
                    tb.wallet.metaMask_Login(bitNum, tableName)
                    tb.carv.carvTask(bitNum, tableName)
                except BaseException:
                    pass

            if 2 in checkboxNum:
                try:
                    tb.wallet.metaMask_Login(bitNum, tableName)
                    tb.layer3.layer3Task(bitNum, tableName)
                except BaseException:
                    pass

            if 3 in checkboxNum:
                try:
                    tb.coingecko.coingeckoTask(bitNum, tableName)
                except BaseException:
                    pass

            if 4 in checkboxNum:
                try:
                    tb.wallet.metaMask_Login(bitNum, tableName)
                    tb.zetalabs.zetaTask(bitNum, tableName)
                except BaseException:
                    pass

            if 5 in checkboxNum:
                try:
                    tb.coingecko.cassavaTask(bitNum, tableName)
                except BaseException:
                    pass

            if 6 in checkboxNum:
                try:
                    tb.coinmarketcap.CollectDiamonds(bitNum, tableName)
                except BaseException:
                    pass

            driver.close()
            driver.quit()
            bitDriver.bit_stopBrowser(bitId)

    @staticmethod
    def adsAllTask(inputNum):
        for x in inputNum:
            # 定义acc为账号id
            adsId = Config.adsId(x)
            # 定义adsNUm为窗口编号
            adsNum = Config.adsNum(x)
            url = "http://local.adspower.net:50325/api/v1/browser/"
            open_url = url + "start?user_id=" + adsId + "&open_tabs=1"
            close_url = url + "stop?user_id=" + adsId
            driver = Driver().Driver(adsId)
            ads = Task(driver)
            tableName = 'ads_task'

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

            if x < 26:
                try:
                    ads.coingecko.soquestTask(adsNum, tableName)
                except BaseException:
                    pass

            try:
                ads.coingecko.cassavaTask(adsNum, tableName)
            except BaseException:
                pass

            driver.quit()
            requests.get(close_url)

    @staticmethod
    def bitAllTask(inputNum):
        for x in inputNum:
            # 定义bitId为账号id
            bitId = Config.bitId(x)
            # 定义bitNum为窗口编号
            bitNum = Config.bitNum(x)

            driver = bitDriver().browser(bitId)
            bit = Task(driver)
            tableName = 'bit_task'

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

            driver.close()
            driver.quit()
            bitDriver.bit_stopBrowser(bitId)
