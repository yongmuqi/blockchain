import time

from taskCode.actions import actionsBase, Config
from taskCode.actions.textFile import textFile


class Wallet:
    # metamask钱包页面的元素
    metamask_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
    metamask_password_xpath = '//*[@id="password"]'
    metamask_login_xpath = '//*[@id="app-content"]/div/div[3]/div/div/button'
    metamask_head_xpath = '//*[@id="app-content"]/div/div[1]/div/div[2]/button'
    #
    metamask_network_list_xpath = '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span'
    metamask_network_list_CLASS_NAME = 'network-name-item'
    metamask_goerli_network = 'Goerli Test'
    metamask_state = 'MetaMask登录成功'
    metamask_buttonX = '//*[@id="app-content"]/div/div[2]/div/div[4]/div/button'
    metamask_signButton = "//button[text()='Sign']"
    metamask_switchNetwork = '//button[@class="button btn--rounded btn-primary"]'
    metamask_empowerConfirm = "//button[text()='Confirm']"
    metamask_confirmButton = "//button[text()='Confirm']"
    add_network_url = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network'
    add_network_name = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input'
    add_network_RPC = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input'
    add_network_ChainID = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input'
    add_network_Symbol = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input'
    add_network_Explorer = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input'
    add_network_Save = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'
    # 数据库表头
    taskName = 'MetaMask'

    def __init__(self, driver):
        self.driver = actionsBase(driver)

    # 狐狸钱包登录功能
    def metamask_login(self, adsNum, tableName):
        password = self.driver.mysql.search_db('others', 1)[1]
        self.driver.browser.navi_to_page(self.metamask_url)
        time.sleep(3)
        self.driver.browser.refresh()
        self.driver.element.send_keys_3sec(self.metamask_password_xpath, password)
        time.sleep(2)
        self.driver.element.click(self.metamask_login_xpath)
        self.driver.mysql.add(tableName, self.taskName, self.metamask_state, adsNum)
        try:
            self.driver.element.click_3sec("//button[text()='Got it']")
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec("//button[text()='Reject']")
        except BaseException:
            pass

    def metamask_firstSign(self):
        self.driver.browser.windows_toggle(1)
        try:
            self.driver.element.click_3sec('//*[@id="popover-content"]/div/div/section/div[3]/button')
        except BaseException:
            pass
        self.driver.element.click('//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]')
        time.sleep(2)
        self.driver.element.click('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
        time.sleep(5)
        self.driver.browser.windows_handles()

    def metamask_addNetwork(self):
        self.driver.browser.windows_toggle(1)
        self.driver.element.click('//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')
        time.sleep(2)
        self.driver.element.click('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]')
        time.sleep(5)
        self.driver.browser.windows_handles()

    # 狐狸钱包签名功能
    def metamask_sign(self):
        self.driver.browser.windows_toggle(1)
        try:
            self.driver.element.click_3sec('//button[@class="button btn--rounded btn-primary"]')
        except BaseException:
            pass
        self.driver.element.click(self.metamask_signButton)
        time.sleep(5)
        self.driver.browser.windows_handles()

    # 狐狸钱包切换网络功能
    def metamask_switch(self):
        self.driver.browser.windows_toggle(1)
        time.sleep(3)
        try:
            self.driver.element.click_3sec("//button[text()='Got it']")
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec('(//i[@role="button"])[1]')
            time.sleep(1)
            self.driver.element.click_3sec('(//i[@role="button"])[1]')
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec("//button[text()='Approve']")
            time.sleep(1)
        except BaseException:
            pass
        self.driver.element.click(self.metamask_switchNetwork)
        time.sleep(3)
        self.driver.browser.windows_handles()

    # 狐狸钱包授权签名功能
    def metamask_empower(self):
        self.driver.browser.windows_toggle(1)
        self.driver.element.click(self.metamask_empowerConfirm)
        time.sleep(5)
        self.driver.browser.windows_handles()

    # 狐狸钱包确定交易功能
    def metamask_submit(self):
        self.driver.browser.windows_toggle(1)
        try:
            self.driver.element.click_3sec('//*[@id="app-content"]/div/div[2]/div/div[4]/div/button')
        except BaseException:
            pass
        # 判断按钮是否可点击，一直等待到按钮返回True（可点击）为止
        self.driver.element.while_button_60sec(self.metamask_confirmButton)
        time.sleep(3)
        self.driver.browser.windows_handles()

    # 切换metamask网络功能(在metamask已登录状态下)
    def metamask_list(self, adsNum, tableName, value):
        try:
            self.metamask_login(adsNum, tableName)
        except BaseException:
            pass
        time.sleep(3)
        self.driver.element.click(self.metamask_network_list_xpath)
        self.driver.element.find_location(self.metamask_network_list_CLASS_NAME, value)

    def suiWallet(self):
        password = Config.password()
        self.driver.browser.windows_toggle(1)
        try:
            self.driver.element.send_keys_3sec('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
            time.sleep(5)
            self.driver.element.clicks('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        except BaseException:
            pass
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]/span')
        self.driver.browser.windows_handles()

    # petra钱包
    def petraWallet(self):
        password = Config.password()
        time.sleep(5)
        self.driver.browser.windows_toggle(1)
        try:
            self.driver.element.send_keys_3sec('//*[@id="field-:r1:"]', password)
            time.sleep(1)
            self.driver.element.click("//button[text()='Unlock']")
        except BaseException:
            pass
        time.sleep(3)
        self.driver.element.while_button_60sec("//button[text()='Approve']")
        time.sleep(5)
        self.driver.browser.windows_handles()

    # Fuel钱包
    def fuel_wallet(self):
        self.driver.browser.windows_toggle(1)
        self.driver.element.while_button_60sec("//button[text()='Connect']")
        time.sleep(5)
        self.driver.browser.windows_handles()

    def fuel_wallet_sign(self):
        password = Config.password()
        self.driver.browser.windows_toggle(1)
        self.driver.element.while_button_60sec("//button[text()='Sign']")
        time.sleep(1)
        self.driver.element.send_keys('//*[@id=":r2:"]', password)
        self.driver.element.click("//button[@type='submit']")
        time.sleep(5)
        self.driver.browser.windows_handles()

    def fuel_wallet_Confirm(self):
        password = Config.password()
        self.driver.browser.windows_toggle(1)
        self.driver.element.while_button_60sec("//button[text()='Confirm']")
        self.driver.element.send_keys('//*[@id=":r6:"]', password)
        self.driver.element.click("//button[@type='submit']")
        time.sleep(5)
        self.driver.browser.windows_handles()

    # argentX钱包
    def argentX_Wallet(self):
        self.driver.browser.windows_toggle(1)
        self.driver.element.while_button_60sec("//button[text()='Approve']")
        time.sleep(5)
        self.driver.browser.windows_handles()

    def argentX_Sign(self):
        self.driver.browser.windows_toggle(1)
        self.driver.element.while_button_60sec("//button[text()='Connect']")
        time.sleep(5)
        self.driver.browser.windows_handles()

    # 添加网络
    def add_network(self, adsNum, tableName):
        name = 'Aztec Testnet'
        rpc = 'https://aztec-connect-testnet-eth-host.aztec.network:8545'
        chainId = '677868'
        symbol = 'ETH'
        exp = 'https://explorer.liberty10.shardeum.org/'
        self.metamask_login(adsNum, tableName)
        self.driver.browser.navi_to_page('https://www.google.com')
        self.driver.browser.navi_to_page(self.add_network_url)
        self.driver.element.send_keys(self.add_network_name, name)
        self.driver.element.send_keys(self.add_network_RPC, rpc)
        self.driver.element.send_keys(self.add_network_ChainID, chainId)
        self.driver.element.send_keys(self.add_network_Symbol, symbol)
        # self.driver.element.send_keys(self.add_network_Explorer, exp)
        self.driver.element.click(self.add_network_Save)
        time.sleep(5)
        textFile.write_txt_data(adsNum + "成功")

    def batch_transfer(self):
        all_adsNum = Config.all_ads()
        for i in range(34, len(all_adsNum) + 1):
            self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div/div/div[2]/div/div[2]/button[2]/span')
            time.sleep(2)
            address = Config.adsAddress(i)
            self.driver.element.clear('//*[@id="app-content"]/div/div[3]/div/div[2]/div/input')
            self.driver.element.send_keys('//*[@id="app-content"]/div/div[3]/div/div[2]/div/input', address)
            time.sleep(3)
            self.driver.element.send_keys('//*[@id="app-content"]/div/div[3]/div/div[3]/div/div[3]/div[2]/div[1]/div/div/div[1]/input', '0.1')
            time.sleep(2)
            self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]')
            time.sleep(2)
            self.driver.element.while_button_60sec(self.metamask_empowerConfirm)
            time.sleep(3)
