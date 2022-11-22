import time

from taskCode.actions import actionsBase


class Wallet:
    # metamask钱包页面的元素
    metamask_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
    metamask_password_xpath = '//*[@id="password"]'
    metamask_login_xpath = '//*[@id="app-content"]/div/div[3]/div/div/button'
    metamask_head_xpath = '//*[@id="app-content"]/div/div[1]/div/div[2]/button'
    metamask_network_list_xpath = '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span'
    metamask_network_list_CLASS_NAME = 'network-name-item'
    metamask_goerli_network = 'Goerli Test'
    metamask_state = 'MetaMask登录成功'
    metamask_buttonX = '//*[@id="app-content"]/div/div[2]/div/div[4]/div/button'
    metamask_signButton = '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]'
    metamask_switchNetwork = '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]'
    metamask_empowerConfirm = '//*[@id="app-content"]/div/div[2]/div/div[5]/footer/button[2]'
    metamask_confirmButton = '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[2]'
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
    def metamask_login(self, adsNum):
        password = self.driver.mysql.search_db('others', 1)[1]
        self.driver.browser.navi_to_page(self.metamask_url)
        self.driver.browser.refresh()
        self.driver.element.send_keys(self.metamask_password_xpath, password)
        time.sleep(2)
        self.driver.element.click(self.metamask_login_xpath)
        self.driver.mysql.add(self.taskName, self.metamask_state, adsNum)

    def metamask_firstSign(self):
        self.driver.browser.windows_toggle(1)
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
        self.driver.element.click(self.metamask_signButton)
        time.sleep(3)
        self.driver.browser.windows_handles()

    # 狐狸钱包切换网络功能
    def metamask_switch(self):
        self.driver.browser.windows_toggle(1)
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
            self.driver.element.click('//*[@id="app-content"]/div/div[2]/div/div[4]/div/button')
        except BaseException:
            pass
        # 判断按钮是否可点击，一直等待到按钮返回True（可点击）为止
        while True:
            button = self.driver.find.xpath_enable(self.metamask_confirmButton)
            if button:
                self.driver.element.click(self.metamask_confirmButton)
                break
        time.sleep(3)
        self.driver.browser.windows_handles()

    # 切换metamask网络功能(在metamask已登录状态下)
    def metamask_list(self, value):
        self.driver.browser.navi_to_page(self.metamask_url)
        self.driver.element.click(self.metamask_network_list_xpath)
        self.driver.element.find_location(self.metamask_network_list_CLASS_NAME, value)

    def suiWallet(self):
        password = self.driver.mysql.search_db('others', 1)[1]
        self.driver.browser.windows_toggle(1)
        try:
            self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
            time.sleep(5)
            self.driver.element.clicks('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        except BaseException:
            pass
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]/span')
        self.driver.browser.windows_handles()

    # 添加网络
    def add_network(self, adsNum):
        name = 'Shardeum Liberty 1.3'
        rpc = 'https://liberty10.shardeum.org'
        chainId = '8080'
        symbol = 'SHM'
        exp = 'https://explorer.liberty10.shardeum.org/'
        self.metamask_login(adsNum)
        self.driver.browser.navi_to_page('https://www.google.com')
        self.driver.browser.navi_to_page(self.add_network_url)
        self.driver.element.send_keys(self.add_network_name, name)
        self.driver.element.send_keys(self.add_network_RPC, rpc)
        self.driver.element.send_keys(self.add_network_ChainID, chainId)
        self.driver.element.send_keys(self.add_network_Symbol, symbol)
        self.driver.element.send_keys(self.add_network_Explorer, exp)
        self.driver.element.click(self.add_network_Save)
        time.sleep(5)
