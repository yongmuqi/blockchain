import datetime
import time

from taskCode.actions import actionsBase
from taskCode.actions.mysql import Query
from .wallet import Wallet


class fusionist:
    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)
        self.q = Query()

    def get_icon(self, adsNum, tableName):
        self.wallet.metamask_list(adsNum, tableName, 'Endurance')
        notion = self.driver.element.get_text("//span[@class='currency-display-component__text']")
        self.q.add(tableName, 'OtherTask3', notion, adsNum)
        allCoin = float(notion)
        lastCoin = 0
        self.driver.browser.navi_to_page('https://ace.fusionist.io/account/endurance')
        try:
            self.driver.find.xpath_element_3sec("//img[contains(@src,'/7')][contains(@style,'0.25')]")
            self.driver.browser.navi_to_page("https://ace.fusionist.io/account/boat#id=7")
            time.sleep(3)
            self.driver.element.click("//button[text()='Claim']")
            time.sleep(5)
            self.wallet.metamask_submit()
            self.driver.find.xpath_notElement_60sec("//button[text()='Claim']")
            lastCoin = allCoin - 0.03
            self.driver.browser.navi_to_page('https://ace.fusionist.io/account/endurance')
        except BaseException:
            lastCoin = allCoin
            pass
        try:
            self.driver.find.xpath_element_3sec("//img[contains(@src,'/8')][contains(@style,'0.25')]")
            self.driver.browser.navi_to_page("https://ace.fusionist.io/account/boat#id=8")
            time.sleep(3)
            self.driver.element.click("//button[text()='Claim']")
            time.sleep(5)
            self.wallet.metamask_submit()
            self.driver.find.xpath_notElement_60sec("//button[text()='Claim']")
            nextCoin = lastCoin - 0.04
            self.driver.browser.navi_to_page('https://ace.fusionist.io/account/endurance')
        except BaseException:
            nextCoin = lastCoin
            pass

        if nextCoin > 0.32:
            self.driver.find.xpath_element_3sec("//img[contains(@src,'/9')][contains(@style,'0.25')]")
            self.driver.browser.navi_to_page("https://ace.fusionist.io/account/boat#id=9")
            time.sleep(3)
            self.driver.element.click("//button[text()='Claim']")
            time.sleep(5)
            self.wallet.metamask_submit()
            self.driver.find.xpath_notElement_60sec("//button[text()='Claim']")


    def fusionist(self, adsNum, tableName):
        self.wallet.metamask_list(adsNum, tableName, 'Endurance')
        notion = self.driver.element.get_text("//span[@class='currency-display-component__text']")
        self.q.add(tableName, 'OtherTask3', notion, adsNum)
        self.driver.browser.navi_to_page('https://ace.fusionist.io/account/endurance')
        time.sleep(5)
        notion = self.driver.element.get_text("//div[@class='css-bcyx6n']")
        now = datetime.datetime.now()
        if "Replenished" in notion:
            if now.hour >= 18:
                self.q.add(tableName, 'OtherTask1', '第二次：' + notion, adsNum)
            else:
                self.q.add(tableName, 'OtherTask1', notion, adsNum)
        else:
            try:
                self.fusionist_dayCheck(tableName, adsNum)
            except BaseException:
                notion = self.driver.element.get_text("//div[@class='css-bcyx6n']")
                hour = int(notion[13:15])
                minute = int(notion[17:19])
                second = int(notion[21:23])
                if hour == 0 and minute == 2 or hour == 0 and minute == 1 or hour == 0 and minute == 3 or hour == 0 and minute == 4:
                    sleepTime = minute * 60 + second + 3
                    time.sleep(sleepTime)
                    self.fusionist_dayCheck(tableName, adsNum)
                elif hour == 0 and minute == 0 and second > 0:
                    sleepTime = second + 3
                    time.sleep(sleepTime)
                    self.fusionist_dayCheck(tableName, adsNum)
                else:
                    if now.hour >= 18:
                        self.q.add(tableName, 'OtherTask1', '第二次：' + notion, adsNum)
                    else:
                        self.q.add(tableName, 'OtherTask1', notion, adsNum)

        try:
            self.fusionist_runCheck(tableName, adsNum)
        except BaseException:
            notion = self.driver.element.get_text("(//div[@class='css-bcyx6n'])[2]")
            now = datetime.datetime.now()
            hour = int(notion[13:15])
            minute = int(notion[17:19])
            second = int(notion[21:23])
            if hour == 0 and minute == 2 or hour == 0 and minute == 1 or hour == 0 and minute == 3 or hour == 0 and minute == 4:
                sleepTime = minute * 60 + second + 3
                time.sleep(sleepTime)
                self.fusionist_runCheck(tableName, adsNum)
            elif hour == 0 and minute == 0 and second > 0:
                sleepTime = second + 3
                time.sleep(sleepTime)
                self.fusionist_runCheck(tableName, adsNum)
            else:
                if now.hour >= 18:
                    self.q.add(tableName, 'OtherTask2', '第二次：' + notion, adsNum)
                else:
                    self.q.add(tableName, 'OtherTask2', notion, adsNum)

        self.wallet.metamask_list(adsNum, tableName, 'Ethereum Mainnet')
        time.sleep(3)

    def fusionist_dayCheck(self, tableName, adsNum):
        time.sleep(5)
        self.driver.element.click_3sec("//div[@class='css-bcyx6n']//button")
        self.driver.element.textChanel("//div[@class='css-bcyx6n']")
        self.q.add(tableName, 'OtherTask1', '签到成功', adsNum)
        now = datetime.datetime.now()
        if now.hour >= 17:
            self.q.add(tableName, 'OtherTask1', '第二次签到成功', adsNum)
        else:
            self.q.add(tableName, 'OtherTask1', '签到成功', adsNum)
        time.sleep(3)

    def fusionist_runCheck(self, tableName, adsNum):
        try:
            self.driver.element.click_3sec("(//button[text()='Connect Wallet'])[2]")
            time.sleep(2)
            self.driver.element.click("//button[text()='MetaMask']")
            time.sleep(3)
        except BaseException:
            pass
        self.driver.element.click_3sec("//div[@class='css-10sz6xe']//button[1]")
        time.sleep(5)
        self.wallet.metamask_submit()
        self.driver.element.textChanel("(//div[@class='css-bcyx6n'])[2]")
        now = datetime.datetime.now()
        if now.hour >= 17:
            self.q.add(tableName, 'OtherTask2', '第二次挖矿挖成功', adsNum)
        else:
            self.q.add(tableName, 'OtherTask2', '挖矿挖成功', adsNum)
        time.sleep(3)