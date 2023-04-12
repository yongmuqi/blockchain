import requests
from actions.driver import Driver
from taskCode.actions import Config
from taskCode.task import taskBase

if __name__ == "__main__":
    all_adsNum = Config.all_ads()
    all_bitNum = Config.all_bit()
    list = [5,16,18,19,20,21,22,24]
    # for x in list:
    for x in range(1, len(all_adsNum)+1):
        # 定义acc为账号id
        adsId = Config.adsId(x)
        # 定义adsNUm为窗口编号
        adsNum = Config.adsNum(x)
        # 定义adsAddress为钱包地址
        adsAddress = Config.adsAddress(x)
        adsName = Config.adsName(x)
        adsMail = Config.adsMail(x)
        adsDiscord = Config.adsDiscord(x)
        # 定义password为密码
        password = Config.password()
        url = "http://local.adspower.net:50325/api/v1/browser/"
        open_url = url + 'start?user_id=' + adsId + '&open_tabs=1'
        close_url = url + "stop?user_id=" + adsId
        driver = Driver.Driver(open_url)
        tb = taskBase(driver)

        oneXpath = '//img[@alt="1️⃣"]'
        twoXpath = '//img[@alt="2️⃣"]'
        threeXpath = '//img[@alt="3️⃣"]'
        fourXpath = '//img[@alt="4️⃣"]'
        try:
            url = 'https://discord.com/channels/915445727600205844/972025568092647454/1063095422551334953'
            tb.discords.answerQuestion(url, oneXpath)
        except BaseException:
            continue
        except TimeoutError:
            continue

        driver.quit()
        requests.get(close_url)

