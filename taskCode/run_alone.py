import requests
from actions.driver import Driver
from actions.drivers import Drivers
from taskCode.actions import Config
from taskCode.task import taskBase


class run_alone:
    def __init__(self, Num):
        self.driver = Drivers()
        # 定义acc为账号id
        self.adsId = Config.adsId(Num)
        # 定义adsNUm为窗口编号
        self.adsNum = Config.adsNum(Num)
        # 定义adsAddress为钱包地址
        self.adsAddress = Config.adsAddress(Num)
        # 定义password为密码
        self.password = Config.password()
        url = "http://local.adspower.net:50325/api/v1/browser/"
        self.open_url = url + "start?user_id=" + self.adsId + "&open_tabs=1"
        self.close_url = url + "stop?user_id=" + self.adsId

    def taskDriver(self):
        driver = self.driver.Driver(self.open_url, self.adsId)
        return driver


if __name__ == "__main__":
    # for x in range(len(ca.accountall)):
    # x = 1
    # # 定义acc为账号id
    # adsId = Config.adsId(x)
    # # 定义adsNUm为窗口编号
    # adsNum = Config.adsNum(x)
    # # 定义adsAddress为钱包地址
    # adsAddress = Config.adsAddress(x)
    # # 定义password为密码
    # password = Config.password()
    # url = "http://local.adspower.net:50325/api/v1/browser/"
    # open_url = url + "start?user_id=" + adsId + "&open_tabs=1"
    # close_url = url + "stop?user_id=" + adsId
    # driver = Driver.Driver(open_url)
    x = 2
    taskDriver = run_alone(x).taskDriver()
    tb = taskBase(taskDriver)

    # try:
    tb.wallet.metamask_login(run_alone(x).adsNum)
    # except BaseException:
    #     pass

    # try:
    #     tb.carv.carv_checkin(adsNum)
    # except BaseException:
    #     pass

    # try:
    #     tb.carv.carv_Dragonball(adsNum)
    # except BaseException:
    #     pass

    # try:
    #     tb.coingecko.coingecko_get(adsNum)
    # except BaseException:
    #     pass

    # try:
    # tb.zetalabs.zeta_getToken(acName)
    # except BaseException:
    #     pass

    taskDriver.quit()
    requests.get(run_alone(x).close_url)
