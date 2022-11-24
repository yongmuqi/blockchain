import threading
import time
import requests
from actions.driver import Driver
from actions.config import Config
from task import taskBase


class run_sign:

    def work(x):
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

        print(x)

        tb.wallet.metamask_login(adsNum)

        # tb.carv.carv_checkin(adsNum)
        #
        # tb.coingecko.coingecko_get(adsNum)

        tb.zetalabs.zeta_swap(adsNum)

        driver.quit()
        requests.get(close_url)

    @staticmethod
    def run_thread(x):
        with sem:
            run_sign.work(x)


if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    threadList = []
    sem = threading.Semaphore(2)
    for i in range(1, len(all_adsNum)+1):
        time.sleep(5)
        thread = threading.Thread(target=run_sign.run_thread, args=(i,))
        threadList.append(thread)
        thread.start()
