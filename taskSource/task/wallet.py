import time

from selenium.webdriver.common.by import By
from taskSource.method import elementMethod, Config


class Wallet:
    # 数据库表头
    taskName = 'MetaMask'

    def __init__(self, driver):
        self.driver = elementMethod(driver)

    # 狐狸钱包登录功能
    def metaMask_Login(self, Num, dbName):
        password = self.driver.mysql.search_db('others', 1)[1]
        self.driver.element_Browser.navi_to_page('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        time.sleep(3)
        try:
            self.driver.element_Wait.wait_visibility_of_element_t(By.XPATH, '//div[@class="spinner loading-overlay__spinner"]', 3)
            self.driver.element_Action.click_t(By.XPATH, '//button[@class="button btn--rounded btn-secondary"]', 60)
            self.driver.element_Action.click("//span[text()='Ethereum Mainnet']")
            time.sleep(2)
        except BaseException:
            pass
        try:
            self.driver.element_Wait.wait_visibility_of_element('//*[@id="password"]')
            self.driver.element_Action.send_keys('//*[@id="password"]', password)
        except BaseException:
            self.driver.element_Browser.refresh()
            self.driver.element_Action.send_keys_t(By.XPATH, '//*[@id="password"]', password, 5)
        time.sleep(2)
        self.driver.element_Action.click('//button[@data-testid="unlock-submit"]')
        self.driver.mysql.add(dbName, self.taskName, 'MetaMask登录成功', Num)
        time.sleep(2)
        # try:
        #     self.driver.element_Action.click_t(By.XPATH, "//button[text()='Got it']", 3)
        # except BaseException:
        #     pass
        # try:
        #     self.driver.element_Action.click_t(By.XPATH, "//button[text()='Reject']", 3)
        # except BaseException:
        #     pass

        # 获取私钥
        # self.driver.element_Action.click('//button[@data-testid="account-options-menu-button"]')
        # self.driver.element_Action.click("//div[text()='Account details']")
        # self.driver.element_Action.click("//button[text()='Export private key']")
        # self.driver.element_Action.send_keys('//input[@type="password"]', '3981786cc')
        # self.driver.element_Action.click("//button[text()='Confirm']")
        # key = self.driver.element_Action.get_text('//div[@class="export-private-key-modal__private-key-display"]')
        # self.driver.mysql.add_wallet('ads_wallet', 'MetamaskKey', key, Num)

    def metaMask_FirstSign(self):
        self.driver.element_Browser.windows_wallet()
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[@class='button btn--rounded btn-primary']", 3)
            time.sleep(2)
            self.driver.element_Action.click('//button[@data-testid="page-container-footer-next"]')
        except BaseException:
            self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="request-signature__sign"]', 3)
        self.driver.element_Browser.windows_handles()

    def metaMask_AddNetWork(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Action.click("//button[@class='button btn--rounded btn-primary']")
        time.sleep(2)
        self.driver.element_Action.click("//button[@class='button btn--rounded btn-primary']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    # 狐狸钱包签名功能
    def metaMask_Sign(self):
        self.driver.element_Browser.windows_wallet()
        try:
            self.driver.element_Action.click_t(By.XPATH, '//button[@class="button btn--rounded btn-primary"]', 3)
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="page-container-footer-next"]', 3)
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="request-signature__sign"]', 3)
        except BaseException:
            pass
        time.sleep(3)
        self.driver.element_Browser.windows_handles()

    # 需要拉倒底部的签名
    def metaMask_downSign(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Action.click('//*[@class="fa fa-arrow-down"]')
        time.sleep(2)
        self.driver.element_Action.click('//button[@data-testid="page-container-footer-next"]')
        time.sleep(2)
        self.driver.element_Browser.windows_handles()

    # 狐狸钱包切换网络功能
    def metaMask_SwitchNetWork(self):
        self.driver.element_Browser.windows_wallet()
        time.sleep(3)
        try:
            self.driver.element_Action.click_t(By.XPATH, '(//i[@role="button"])[1]', 3)
            time.sleep(1)
            self.driver.element_Action.click('(//i[@role="button"])[1]')
        except BaseException:
            pass
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Approve']", 3)
            time.sleep(1)
        except BaseException:
            pass
        self.driver.element_Action.click_t(By.XPATH, '//button[@class="button btn--rounded btn-primary"]', 3)
        time.sleep(3)
        self.driver.element_Browser.windows_handles()

    # 狐狸钱包授权签名功能
    def metaMask_Empower(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Function.wait_and_click_button("//button[text()='Confirm']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    # 狐狸钱包确定交易功能
    def metaMask_Submit(self):
        self.driver.element_Browser.windows_wallet()
        try:
            self.driver.element_Action.click_t(By.XPATH, "//button[text()='Got it']", 3)
        except BaseException:
            pass
        self.driver.element_Browser.set_window_size()
        # 判断按钮是否可点击，一直等待到按钮返回True（可点击）为止
        self.driver.element_Function.wait_and_click_button("//button[text()='Confirm']")
        time.sleep(3)
        self.driver.element_Browser.windows_handles()

    # 狐狸钱包确定交易功能-自定义
    def metaMask_Submit_custom(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Action.click("//span[text()='Max']")
        self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="page-container-footer-next"]', 3)
        self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="page-container-footer-next"]', 3)
        time.sleep(2)
        self.driver.element_Browser.windows_handles()

    #
    def metaMask_Submit_sendCustom(self):
        self.driver.element_Browser.windows_wallet()
        time.sleep(2)
        self.driver.element_Action.send_keys('//input[@placeholder="Enter a number"]', 4)
        self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="page-container-footer-next"]', 3)
        self.driver.element_Action.click_t(By.XPATH, '//button[@data-testid="page-container-footer-next"]', 3)
        time.sleep(2)
        self.driver.element_Browser.windows_handles()

    # 切换metamask网络功能(在metamask已登录状态下)
    def metamask_List(self, adsNum, dbName, value):
        try:
            self.metaMask_Login(adsNum, dbName)
        except BaseException:
            pass
        time.sleep(3)
        self.driver.element_Action.click('//div[@data-testid="network-display"]')
        self.driver.element_Function.find_location('network-name-item', value)

    def suiWallet(self):
        password = Config.password()
        self.driver.element_Browser.windows_wallet()
        try:
            self.driver.element_Action.send_keys_t(By.XPATH, '//*[@id="root"]/div/div/div[2]/main/div/form/label/input', 3, password)
            time.sleep(5)
            self.driver.element_Action.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        except BaseException:
            pass
        self.driver.element_Action.click('//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]/span')
        self.driver.element_Browser.windows_handles()

    # petra钱包
    def petraWallet(self):
        password = Config.password()
        self.driver.element_Browser.windows_wallet()
        try:
            self.driver.element_Action.send_keys_t(By.XPATH, '//*[@id="field-:r1:"]', 3, password)
            time.sleep(1)
            self.driver.element_Action.click("//button[text()='Unlock']")
        except BaseException:
            pass
        time.sleep(3)
        self.driver.element_Function.wait_and_click_button("//button[text()='Approve']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    # Fuel钱包
    def fuel_wallet(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Function.wait_and_click_button("//button[text()='Connect']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    def fuel_wallet_sign(self):
        password = Config.password()
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Function.wait_and_click_button("//button[text()='Sign']")
        time.sleep(1)
        self.driver.element_Action.send_keys('//*[@id=":r2:"]', password)
        self.driver.element_Action.click("//button[@type='submit']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    def fuel_wallet_Confirm(self):
        password = Config.password()
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Function.wait_and_click_button("//button[text()='Confirm']")
        self.driver.element_Action.send_keys('//*[@id=":r6:"]', password)
        self.driver.element_Action.click("//button[@type='submit']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    # argentX钱包
    def argentX_Wallet(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Function.wait_and_click_button("//button[text()='Approve']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    def argentX_Sign(self):
        self.driver.element_Browser.windows_wallet()
        self.driver.element_Function.wait_and_click_button("//button[text()='Connect']")
        time.sleep(5)
        self.driver.element_Browser.windows_handles()

    # 狐狸钱包转载功能
    def batch_transfer(self):
        all_adsNum = Config.all_ads()
        for i in range(34, len(all_adsNum) + 1):
            self.driver.element_Action.click('//*[@id="app-content"]/div/div[3]/div/div/div/div[2]/div/div[2]/button[2]/span')
            time.sleep(2)
            address = Config.adsAddress(i)
            self.driver.element_Action.clear('//*[@id="app-content"]/div/div[3]/div/div[2]/div/input')
            self.driver.element_Action.send_keys('//*[@id="app-content"]/div/div[3]/div/div[2]/div/input', address)
            time.sleep(3)
            self.driver.element_Action.send_keys('//*[@id="app-content"]/div/div[3]/div/div[3]/div/div[3]/div[2]/div[1]/div/div/div[1]/input', '0.1')
            time.sleep(2)
            self.driver.element_Action.click('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]')
            time.sleep(2)
            self.driver.element_Function.wait_and_click_button("//button[text()='Confirm']")
            time.sleep(3)

    def checkToken(self, Num, dbName):
        self.metaMask_Login(Num, dbName)
        self.driver.element_Action.click('//div[@class="identicon__address-wrapper"]')
        self.driver.element_Action.click("//div[text()='Settings']")
        self.driver.element_Action.click("//div[text()='Security & privacy']")
        try:
            self.driver.element_Action.click('//label[@class="toggle-button toggle-button--off"]')
            time.sleep(2)
        except BaseException:
            print(str(Num) + '失败')