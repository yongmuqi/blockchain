import time
from selenium.webdriver.common.by import By

from taskSource.function.textFile import textFile
from taskSource.method import elementMethod
from taskSource.method import Mysql
from taskSource.task.wallet import Wallet


class Others:
    def __init__(self, driver):
        self.driver = elementMethod(driver)
        self.wallet = Wallet(driver)
        self.mysql = Mysql()

    def zetaQuest(self, address, Num, tableName):
        self.driver.element_Browser.navi_to_page('https://docs.google.com/forms/d/e/1FAIpQLSeEU-k4UpVquAue374i3RPbsdCF2KM5Kz_q-nYG_IBr-C87DQ/viewform')
        time.sleep(3)
        self.driver.element_Action.send_keys('//input[@class="whsOnd zHQkBf"]', address)
        self.driver.element_Action.click("//span[text()='Athens testnet']")
        self.driver.element_Action.click("//span[text()='ZETA']")
        self.driver.element_Action.click("//span[text()='Paying gas fees for ZetaChain smart contracts & securing the PoS ZetaChain blockchain by bonding/staking/slashing']")
        self.driver.element_Action.click("//span[text()='ZetaScan']")
        self.driver.element_Action.click("//span[text()='5 million+']")
        self.driver.element_Action.click("//span[text()='Validators, Observers, & Signers']")
        self.driver.element_Action.click("//span[text()='$2 billion+']")
        self.driver.element_Action.click('//span[@class="l4V7wb Fxmcue"]')
        self.driver.element_Wait.wait_visibility_of_element('//span[@class="NPEfkd RveJvd snByac"]')
        self.mysql.add(tableName, 'OtherTask2', "zeta答题成功", Num)
        time.sleep(5)

    def zetaGalxe(self):
        self.driver.element_Browser.navi_to_page('https://galxe.com/ZetaChain/campaign/GC8fMU4Ced')
        time.sleep(5)
        self.driver.element_Action.click("//span[contains(text(),'Switch to POLYGON')]")

    def scrollTask(self, Num):
        self.driver.element_Browser.maxWindows()
        # UNI-SCROLL任务
        self.driver.element_Browser.navi_to_page('https://uniswap-v3.scroll.io/#/swap?outputCurrency=0xA0D71B9877f44C744546D649147E3F1e70a93760')
        time.sleep(5)
        try:
            self.driver.element_Action.click_t(By.XPATH, '//button[@class="sc-bczRLJ lfsInV sc-fwrjc2-0 sc-fwrjc2-1 sc-1ovkkl7-5 fqnNcc hflwPT jKyIHm"]', 60)
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, "//*[text()='English']", 3)
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Connect']", 3)
            time.sleep(1)
            self.driver.element_Action.click("//div[text()='MetaMask']")
            self.wallet.metaMask_FirstSign()
        except BaseException:
            pass
        try:
            time.sleep(3)
            self.driver.element_Action.click_t(By.XPATH, "(//span[text()='Unsupported'])[2]", 3)
            self.driver.element_Action.click("//div[text()='Scroll Alpha']")
            self.wallet.metaMask_SwitchNetWork()
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Connect']", 3)
            time.sleep(1)
            self.driver.element_Action.click("//div[text()='MetaMask']")
        except BaseException:
            pass

        coin = self.driver.element_Action.get_text('(//div[@class="sc-sx9n2y-0 kandXm css-zhpkf8"])[4]')
        # 从字符串中提取数字
        digits = ''.join(filter(str.isdigit, coin))
        print(digits)
        if int(digits) == 0:
            self.driver.element_Action.click("(//button[contains(@class,'sc-bczRLJ lfsInV')])[2]")
            time.sleep(1)
            self.driver.element_Action.click("//div[text()='Ether']")
            time.sleep(1)
            # self.driver.element_Action.click("(//div[@class='sc-3zewi2-4 eiTjnJ']//button)[2]")
            # self.driver.element_Action.click("//div[text()='USD Coin']")
            self.driver.element_Action.send_keys('//input[@inputmode="decimal"]', 0.005)
            self.driver.element_Function.wait_and_click_button('//button[@id="swap-button"]')
            try:
                self.driver.element_Action.click_t(By.XPATH, "//button[text()='Accept']", 3)
            except BaseException:
                pass
            self.driver.element_Action.click('//button[@id="confirm-swap-or-send"]')
            self.wallet.metaMask_Submit()
            try:
                self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//div[text()="Success"]', 20)
            except BaseException:
                textFile.write_txt_data(Num + "此窗口SWAP失败")
        else:
            pass

        self.driver.element_Browser.navi_to_page('https://uniswap-v3.scroll.io/#/pool')
        time.sleep(3)
        self.driver.element_Action.click('//*[@data-cy="join-pool-button"]')


        self.driver.element_Action.click("//span[text()='Select a token']")
        self.driver.element_Action.click("//div[text()='USD Coin']")
        self.driver.element_Action.click("//div[text()='1%']")
        self.driver.element_Action.click("//div[text()='Full Range']")
        self.driver.element_Action.click("//div[text()='I understand']")
        self.driver.element_Action.send_keys('//input[@inputmode="decimal"]', 0.003)
        try:
            self.driver.element_Action.click("(//button[contains(@class,'sc-bczRLJ jEYeSq')])[2]")
            self.wallet.metaMask_Submit_custom()
        except BaseException:
            pass
        self.driver.element_Function.wait_and_click_button("//div[@id='root']/div[1]/div[2]/div[4]/main[1]/div[2]/div[1]/div[4]/div[3]/div[1]/button[1]")
        self.driver.element_Action.click("//div[text()='Add']")
        self.wallet.metaMask_Submit()

        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//div[text()="Success"]', 20)
            print('2')
            self.driver.element_Action.click("//div[text()='Close']")
            self.driver.element_Action.click("//div[text()='In range']")
            self.driver.element_Action.click("//*[text()='Remove Liquidity']")
            self.driver.element_Action.click("//button[text()='25%']")
            time.sleep(2)
            self.driver.element_Action.click("//button[text()='Remove']")
            time.sleep(1)
            self.driver.element_Action.click("(//button[text()='Remove'])[2]")
            self.wallet.metaMask_Submit()
            notion = self.driver.element_Action.get_text('//div[text()="Success"]')
            print(notion)
            # self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//div[text()="Success"]', 20)
            time.sleep(3)
            textFile.write_txt_data(Num + "成功")
        except BaseException:
            textFile.write_txt_data(Num + "此窗口添加流动性失败")

    def Araya(self):
        self.driver.element_Browser.navi_to_page('chrome-extension://hmpdmfjbbmangocgengldjmbleonbidf/index.html')
        time.sleep(2)
        self.driver.element_Action.send_keys('//input[@placeholder="Password..."]', '3981786cc')
        time.sleep(2)
        self.driver.element_Action.click('//button[@class="chakra-button css-phm4fp"]')
        time.sleep(3)
