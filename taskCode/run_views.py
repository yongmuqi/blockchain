import requests

from taskCode.actions import Config
from taskCode.actions.driver import Driver
from taskCode.task import taskBase
from taskCode.actions.bitDriver import bitDriver


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
            driver = Driver.Driver(open_url)
            tb = taskBase(driver)
            tableName = 'ads_task'

            if 1 in checkboxNum:
                try:
                    tb.wallet.metamask_login(adsNum, tableName)
                    tb.carv.carv_checkin(adsNum, tableName)
                except BaseException:
                    pass

            if 2 in checkboxNum:
                try:
                    tb.wallet.metamask_login(adsNum, tableName)
                    tb.layer3.layer3(adsNum, tableName)
                except BaseException:
                    pass

            if 3 in checkboxNum:
                try:
                    tb.coingecko.coingecko_get(adsNum, tableName)
                except BaseException:
                    pass

            if 4 in checkboxNum:
                try:
                    tb.wallet.metamask_login(adsNum, tableName)
                    tb.zetalabs.zeta_getToken(adsNum, tableName)
                except BaseException:
                    pass

            if 5 in checkboxNum:
                try:
                    tb.layer3.cassava(adsNum, tableName)
                except BaseException:
                    pass

            if 6 in checkboxNum:
                try:
                    tb.wallet.metamask_login(adsNum, tableName)
                    tb.layer3.soquest(adsNum, tableName)
                except BaseException:
                    pass

            if 7 in checkboxNum:
                tb.fusionist.fusionist(adsNum, tableName)

            if 8 in checkboxNum:
                tb.layer3.soquest(adsNum, tableName)

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
            tb = taskBase(driver)
            tableName = 'bit_task'

            if 1 in checkboxNum:
                try:
                    tb.wallet.metamask_login(bitNum, tableName)
                    tb.carv.carv_checkin(bitNum, tableName)
                except BaseException:
                    pass

            if 2 in checkboxNum:
                try:
                    tb.wallet.metamask_login(bitNum, tableName)
                    tb.layer3.layer3(bitNum, tableName)
                except BaseException:
                    pass

            if 3 in checkboxNum:
                try:
                    tb.coingecko.coingecko_get(bitNum, tableName)
                except BaseException:
                    pass

            if 4 in checkboxNum:
                try:
                    tb.wallet.metamask_login(bitNum, tableName)
                    tb.zetalabs.zeta_getToken(bitNum, tableName)
                except BaseException:
                    pass

            if 5 in checkboxNum:
                try:
                    tb.layer3.cassava(bitNum, tableName)
                except BaseException:
                    pass

            if 6 in checkboxNum:
                tb.fusionist.fusionist(bitNum, tableName)

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
            driver = Driver.Driver(open_url)
            ads = taskBase(driver)
            tableName = 'ads_task'

            try:
                ads.wallet.metamask_login(adsNum, tableName)
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

            try:
                ads.zetalabs.zeta_getToken(adsNum, tableName)
            except BaseException:
                pass

            if x < 26:
                try:
                    ads.layer3.soquest(adsNum, tableName)
                except BaseException:
                    pass

            try:
                ads.layer3.cassava(adsNum, tableName)
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
            bit = taskBase(driver)
            tableName = 'bit_task'

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

            bitDriver.bit_stopBrowser(bitId)
