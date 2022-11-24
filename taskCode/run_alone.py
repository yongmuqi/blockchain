import requests
from actions.driver import Driver
from taskCode.actions import Config
from taskCode.task import taskBase

if __name__ == "__main__":
    # for x in range(len(ca.accountall)):
    x = 1
    # 定义acc为账号id
    adsId = Config.adsId(x)
    # 定义adsNUm为窗口编号
    adsNum = Config.adsNum(x)
    # 定义adsAddress为钱包地址
    adsAddress = Config.adsAddress(x)
    # 定义password为密码
    password = Config.password()
    url = "http://local.adspower.net:50325/api/v1/browser/"
    open_url = url + "start?user_id=" + adsId + "&open_tabs=1"
    close_url = url + "stop?user_id=" + adsId
    driver = Driver.Driver(open_url)
    tb = taskBase(driver)

    try:
        tb.wallet.metamask_login(adsNum)
    except BaseException:
        pass

    try:
        tb.carv.carv_checkin(adsNum)
    except BaseException:
        pass

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

    driver.quit()
    requests.get(close_url)
