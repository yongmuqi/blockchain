import time
from selenium.webdriver.common.by import By

from taskSource.function.textFile import textFile
from taskSource.method import elementMethod, Config
from taskSource.method import Mysql
from taskSource.task.wallet import Wallet


class Scroll:
    def __init__(self, driver):
        self.driver = elementMethod(driver)
        self.wallet = Wallet(driver)
        self.mysql = Mysql()

    def scrollTask(self, Num, tableName):
        self.driver.element_Browser.navi_to_page("https://scroll.io/alpha/bridge")
        time.sleep(5)
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Connect Wallet']", 3)
            self.driver.element_Wait.wait_execute_script(
                'document.querySelector("body > onboard-v2").shadowRoot.querySelector("section > div > div > div > div > div > div > div > div.scroll-container.svelte-1n0mo1q > div.svelte-1n0mo1q > div > div > button > span").click()')
        except BaseException:
            pass
        try:
            self.wallet.metaMask_FirstSign()
            self.wallet.metaMask_SwitchNetWork()
        except BaseException:
            pass
        # try:
        #     self.wallet.metaMask_SwitchNetWork()
        # except BaseException:
        #     pass
        Balance = self.driver.element_Action.get_text_t(By.XPATH, "//h6[contains(@class,'MuiTypography-root MuiTypography-subtitle2')]", 20)
        inputNum = Balance.split(": ")[1]
        print(float(inputNum) / 2)
        self.driver.element_Action.send_keys("//input[@placeholder='0.00']", float(inputNum) / 2)
        time.sleep(3)
        self.driver.element_Action.click("//button[text()='Send ']")
        self.wallet.metaMask_Submit()
        self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//button[text()='Move More Funds']", 30)
        self.mysql.add(tableName, 'OtherTask1', "Goerli跨链成功", Num)
        time.sleep(5)

    def scroll_uni_task(self, Num):
        self.scroll_uni_login()
        self.scroll_uni_swap(Num)
        self.scroll_uni_addPool(Num)

    def scroll_uni_login(self):
        # self.driver.element_Browser.maxWindows()
        # UNI-SCROLL任务
        self.driver.element_Browser.navi_to_page(
            'https://uniswap-v3.scroll.io/#/swap?outputCurrency=0xA0D71B9877f44C744546D649147E3F1e70a93760')
        time.sleep(5)
        # try:
        #     self.driver.element_Action.click_t(By.XPATH, '//button[@class="sc-bczRLJ lfsInV sc-fwrjc2-0 sc-fwrjc2-1 sc-1ovkkl7-5 fqnNcc hflwPT jKyIHm"]', 30)
        # except BaseException:
        #     pass
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

    def scroll_uni_swap(self, Num):
        coin = self.driver.element_Action.get_text('(//div[@class="sc-sx9n2y-0 kandXm css-zhpkf8"])[4]')
        # 从字符串中提取数字
        digits = ''.join(filter(str.isdigit, coin))
        print(digits)
        if int(digits) == 0:
            self.driver.element_Action.click("(//button[contains(@class,'sc-bczRLJ lfsInV')])[2]")
            time.sleep(1)
            self.driver.element_Action.click("//div[text()='Ether']")
            time.sleep(1)
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

    def scroll_uni_addPool(self, Num):
        self.driver.element_Browser.navi_to_page('https://uniswap-v3.scroll.io/#/pool')
        time.sleep(3)
        try:
            self.scroll_uni_rePool(Num)
        except BaseException:
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
            self.driver.element_Function.wait_and_click_button( "//div[@id='root']/div[1]/div[2]/div[4]/main[1]/div[2]/div[1]/div[4]/div[3]/div[1]/button[1]")
            self.driver.element_Action.click("//div[text()='Add']")
            self.wallet.metaMask_Submit()
            try:
                self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//div[text()="Success"]', 20)
                self.driver.element_Action.click("//div[text()='Close']")
                time.sleep(5)
            except BaseException:
                textFile.write_txt_data(Num + "此窗口添加流动性失败")
            self.scroll_uni_rePool(Num)

    def scroll_uni_rePool(self, Num):
        self.driver.element_Action.click("//div[text()='In range']")
        self.driver.element_Action.click("//*[text()='Remove Liquidity']")
        self.driver.element_Action.click("//button[text()='25%']")
        time.sleep(2)
        self.driver.element_Action.click("//button[text()='Remove']")
        time.sleep(1)
        self.driver.element_Action.click("(//button[text()='Remove'])[2]")
        self.wallet.metaMask_Submit()
        notion = self.driver.element_Action.get_text('//div[text()="Success"]')
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//div[text()="Success"]', 20)
        except BaseException:
            textFile.write_txt_data(Num + "移除流动性失败")
        time.sleep(3)
        textFile.write_txt_data(Num + "成功")

    def scroll_zkSync_Task(self, Num):
        self.scroll_zkSync_login()
        self.scroll_zkSync_swap(Num)
        self.scroll_zkSync_pool(Num)
        self.scroll_zkSync_repool(Num)
        textFile.write_txt_data(Num + "成功")

    def scroll_zkSync_login(self):
        # self.driver.element_Browser.maxWindows()
        self.driver.element_Browser.navi_to_page('https://staging.syncswap.xyz/')
        time.sleep(5)
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Start']", 3)
            self.driver.element_Action.click("//*[text()='Next']")
            time.sleep(1)
            self.driver.element_Action.click("//*[text()='Next']")
            time.sleep(1)
            self.driver.element_Action.click("//*[text()='Done']")
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, "//p[text()='Mainnet']", 5)
            self.driver.element_Action.click("//p[text()='Scroll Alpha']")
            self.driver.element_Action.click("//button[text()='Switch network']")
            self.wallet.metaMask_SwitchNetWork()
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Connect']", 5)
            time.sleep(2)
            self.driver.element_Action.click("//p[text()='Ethereum Wallet']")
            self.wallet.metaMask_FirstSign()
        except BaseException:
            pass

    def scroll_zkSync_swap(self, Num):
        self.driver.element_Action.send_keys("//input[@class='swap-input']", 0.005)
        self.driver.element_Action.click("//button[text()='Swap']")
        self.wallet.metaMask_Submit()
        time.sleep(10)
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//p[contains(text(),'Confirmed in ')]", 30)
        except BaseException:
            self.driver.element_Action.click("//button[text()='Close']")
            self.driver.element_Action.send_keys("//input[@class='swap-input']", 0.005)
            self.driver.element_Action.click("//button[text()='Swap']")
            self.wallet.metaMask_Submit()
            time.sleep(10)
            try:
                self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//p[contains(text(),'Confirmed in ')]", 30)
            except BaseException:
                textFile.write_txt_data(Num + "swap失败")

    def scroll_zkSync_pool(self, Num):
        self.driver.element_Browser.navi_to_page('https://staging.syncswap.xyz/pool')
        time.sleep(3)
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//p[text()='/']", 5)
        except BaseException:
            self.driver.element_Action.click("//div[text()='New Position']")
            self.driver.element_Action.click("//p[text()='Enter Pool']")
            self.driver.element_Action.click("//p[text()='Deposit']")
            self.driver.element_Action.click("//span[contains(@class,'MuiSwitch-switchBase MuiSwitch-colorPrimary')]")
            self.driver.element_Action.send_keys('(//input[@class="add-liquidity-input"])[2]', 0.003)
            self.driver.element_Action.click("//div[text()='Permit ']")
            self.wallet.metaMask_downSign()
            self.driver.element_Action.click("//button[text()='Deposit']")
            self.wallet.metaMask_Submit()
            time.sleep(10)
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//p[contains(text(),'Confirmed in ')]", 30)
        except BaseException:
            textFile.write_txt_data(Num + "添加流动性失败")

    def scroll_zkSync_repool(self, Num):
        self.driver.element_Browser.navi_to_page('https://staging.syncswap.xyz/pool')
        time.sleep(3)
        self.driver.element_Action.click_t(By.XPATH, "//p[text()='/']", 20)
        self.driver.element_Action.click("//p[text()='Withdraw']")
        self.driver.element_Action.click("//button[text()='25%']")
        self.driver.element_Action.click("//div[contains(text(),'Permit')]")
        self.wallet.metaMask_downSign()
        self.driver.element_Action.click("//button[text()='Withdraw Liquidity']")
        self.wallet.metaMask_Submit()
        time.sleep(10)
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//p[contains(text(),'Confirmed in ')]", 30)
        except BaseException:
            self.driver.element_Action.click("//button[text()='Close']")
            self.driver.element_Action.click("//button[text()='Withdraw Liquidity']")
            self.wallet.metaMask_Submit()
            try:
                self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, "//p[contains(text(),'Confirmed in ')]", 30)
            except BaseException:
                textFile.write_txt_data(Num + "移除流动性失败")
