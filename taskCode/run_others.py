import requests
from actions.driver import Driver
from taskCode.actions import Config
from taskCode.task import taskBase

if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    list = [17, 23, 25, 40]
    for x in list:
        # x = x + 28
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

        # try:
        #     tb.metamask.metamask_login(adsNum)
        # except BaseException:
        #     continue

        # try:
        #     url = 'https://discord.com/channels/915445727600205844/972025568092647454/1045338040089985044'
        #     tb.discord.discord_answer('1.png', '2.png', url, 2, 1)
        # except BaseException:
        #     continue
        # except TimeoutError:
        #     continue

        # tb.other.AVAXFaucet(acName, acAddress)
        tb.twitter.sendTwitter(adsNum)

        driver.quit()
        requests.get(close_url)
