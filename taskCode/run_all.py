import threading
import time
import requests
from actions.driver import Driver
from actions.mysql import Query
from task import taskBase


class run_sign:
    @staticmethod
    def work(x):
        ads_config = Query().search_db('ads_config', x)
        others = Query().search_db('others', 1)
        # 定义acc为账号id
        adsId = ads_config[1]
        # 定义adsNUm为窗口编号
        adsNum = ads_config[2]
        # 定义adsAddress为钱包地址
        adsAddress = ads_config[3]
        # 定义password为密码
        password = others[1]
        url = "http://local.adspower.net:50325/api/v1/browser/"
        open_url = url + "start?user_id=" + adsId + "&open_tabs=1"
        close_url = url + "stop?user_id=" + adsId
        driver = Driver.Driver(open_url)
        tb = taskBase(driver)

        # tb.wallet.metamask_login(adsNum)

        # tb.carv.carv_checkin(adsNum)
        #
        # tb.coingecko.coingecko_get(adsNum)

        # tb.zetalabs.zeta_swap(adsNum)

        try:
            url = 'https://discord.com/channels/915445727600205844/972025568092647454/1040264609589891186'
            tb.discord.discord_answer('1.png', '2.png', url, 3, 4)
        except BaseException:
            pass
        except TimeoutError:
            pass

        driver.quit()
        requests.get(close_url)

    @staticmethod
    def run_thread(x):
        with sem:
            run_sign.work(x)


if __name__ == "__main__":
    ts = []
    sem = threading.Semaphore(1)
    for i in range(1, 2):
        # i = i + 49
        time.sleep(5)
        # b.work(i)
        t = threading.Thread(target=run_sign.run_thread, args=(i,))
        ts.append(t)
        t.start()
