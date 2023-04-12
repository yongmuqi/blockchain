import datetime
import time

from selenium.webdriver.common.by import By
from taskSource.method import elementMethod
from taskSource.method import Mysql
from .wallet import Wallet


def failList():
    ads_fusionistCheckFail = Mysql().findDate('ads_task', 'OtherTask1', '没有内容')
    ads_fusionistDrawFail = Mysql().findDate('ads_task', 'OtherTask2', '没有内容')
    bit_fusionistCheckFail = Mysql().findDate('bit_task', 'OtherTask1', '没有内容')
    bit_fusionistDrawFail = Mysql().findDate('bit_task', 'OtherTask2', '没有内容')
    ads2_fusionistCheckFail = Mysql().findDate_No('ads_task', 'OtherTask1', '二')
    ads2_fusionistDrawFail = Mysql().findDate_No('ads_task', 'OtherTask2', '二')
    bit2_fusionistCheckFail = Mysql().findDate_No('bit_task', 'OtherTask1', '二')
    bit2_fusionistDrawFail = Mysql().findDate_No('bit_task', 'OtherTask2', '二')

    ads_fusionistCheckList = []
    ads_fusionistDrawList = []
    bit_fusionistCheckList = []
    bit_fusionistDrawList = []

    nowTime = datetime.datetime.now()
    if nowTime.hour < 18:
        for failNum in ads_fusionistCheckFail:
            ads_fusionistCheckList.append(int(failNum))
        for failNum in ads_fusionistDrawFail:
            ads_fusionistDrawList.append(int(failNum))
        for failNum in bit_fusionistCheckFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistCheckList.append(int(failNum))
        for failNum in bit_fusionistDrawFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistDrawList.append(int(failNum))
    else:
        for failNum in ads2_fusionistCheckFail:
            ads_fusionistCheckList.append(int(failNum))
        for failNum in ads2_fusionistDrawFail:
            ads_fusionistDrawList.append(int(failNum))
        for failNum in bit2_fusionistCheckFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistCheckList.append(int(failNum))
        for failNum in bit2_fusionistDrawFail:
            if int(failNum) > 65 or int(failNum) == 34:
                pass
            else:
                bit_fusionistDrawList.append(int(failNum))

    ads_fusionistCheckList.extend(ads_fusionistDrawList)
    ads_fusionistFail = []
    for ads_i in ads_fusionistCheckList:
        if ads_i not in ads_fusionistFail:
            ads_fusionistFail.append(ads_i)
    print(ads_fusionistFail)

    bit_fusionistCheckList.extend(bit_fusionistDrawList)
    bit_fusionistFail = []
    for bit_i in bit_fusionistCheckList:
        if bit_i not in bit_fusionistFail:
            bit_fusionistFail.append(bit_i)
    print(bit_fusionistFail)

    return ads_fusionistFail, bit_fusionistFail


class Fusionist:
    def __init__(self, driver):
        self.driver = elementMethod(driver)
        self.wallet = Wallet(driver)
        self.mysql = Mysql()

    def fusionist(self, Num, tableName):
        self.driver.element_Browser.navi_to_page('https://ace.fusionist.io/account/endurance')
        time.sleep(5)
        notion = self.driver.element_Action.get_text("//div[@class='css-bcyx6n']")
        now = datetime.datetime.now()
        if "Replenished" in notion:
            if now.hour >= 18:
                self.mysql.add(tableName, 'OtherTask1', '第二次：' + notion, Num)
            else:
                self.mysql.add(tableName, 'OtherTask1', notion, Num)
        else:
            try:
                self.fusionist_dayCheck(tableName, Num)
            except BaseException:
                notion = self.driver.element_Action.get_text("//div[@class='css-bcyx6n']")
                hour = int(notion[13:15])
                minute = int(notion[17:19])
                second = int(notion[21:23])
                if hour == 0 and minute == 2 or hour == 0 and minute == 1 or hour == 0 and minute == 3 or hour == 0 and minute == 4:
                    sleepTime = minute * 60 + second + 3
                    time.sleep(sleepTime)
                    self.fusionist_dayCheck(tableName, Num)
                elif hour == 0 and minute == 0 and second > 0:
                    sleepTime = second + 3
                    time.sleep(sleepTime)
                    self.fusionist_dayCheck(tableName, Num)
                else:
                    if now.hour >= 18:
                        self.mysql.add(tableName, 'OtherTask1', '第二次：' + notion, Num)
                    else:
                        self.mysql.add(tableName, 'OtherTask1', notion, Num)

        try:
            self.fusionist_runCheck(tableName, Num)
        except BaseException:
            notion = self.driver.element_Action.get_text("(//div[@class='css-bcyx6n'])[2]")
            now = datetime.datetime.now()
            hour = int(notion[13:15])
            minute = int(notion[17:19])
            second = int(notion[21:23])
            if hour == 0 and minute == 2 or hour == 0 and minute == 1 or hour == 0 and minute == 3 or hour == 0 and minute == 4:
                sleepTime = minute * 60 + second + 3
                time.sleep(sleepTime)
                self.fusionist_runCheck(tableName, Num)
            elif hour == 0 and minute == 0 and second > 0:
                sleepTime = second + 3
                time.sleep(sleepTime)
                self.fusionist_runCheck(tableName, Num)
            else:
                if now.hour >= 18:
                    self.mysql.add(tableName, 'OtherTask2', '第二次：' + notion, Num)
                else:
                    self.mysql.add(tableName, 'OtherTask2', notion, Num)
        time.sleep(3)

    def fusionist_dayCheck(self, tableName, adsNum):
        time.sleep(5)
        self.driver.element_Action.click_t(By.XPATH, "//div[@class='css-bcyx6n']//button", 3)
        self.driver.element_Function.wait_for_text_change("//div[@class='css-bcyx6n']")
        self.mysql.add(tableName, 'OtherTask1', '签到成功', adsNum)
        now = datetime.datetime.now()
        if now.hour >= 17:
            self.mysql.add(tableName, 'OtherTask1', '第二次签到成功', adsNum)
        else:
            self.mysql.add(tableName, 'OtherTask1', '签到成功', adsNum)
        time.sleep(3)

    def fusionist_runCheck(self, tableName, adsNum):
        runCheckText = self.driver.element_Action.get_text_t(By.XPATH, "(//div[@class='css-bcyx6n'])[2]", 3)
        if runCheckText == 'Switch Network':
            self.driver.element_Action.click("(//div[@class='css-bcyx6n'])[2]")
            self.wallet.metaMask_SwitchNetWork()
        elif runCheckText == 'Connect Wallet':
            self.driver.element_Action.click_t(By.XPATH, "(//button[text()='Connect Wallet'])[2]", 3)
            time.sleep(2)
            self.driver.element_Action.click("//button[text()='MetaMask']")
            time.sleep(3)
        self.driver.element_Action.click_t(By.XPATH, "//div[@class='css-10sz6xe']//button[1]", 10)
        self.wallet.metaMask_Submit()
        self.driver.element_Function.wait_for_text_change("(//div[@class='css-bcyx6n'])[2]")
        now = datetime.datetime.now()
        if now.hour >= 17:
            self.mysql.add(tableName, 'OtherTask2', '第二次挖矿挖成功', adsNum)
        else:
            self.mysql.add(tableName, 'OtherTask2', '挖矿挖成功', adsNum)
        time.sleep(3)
