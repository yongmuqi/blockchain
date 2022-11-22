import time

from taskCode.actions import actionsBase
from selenium.webdriver import Keys


class Scroll:
    metamask_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
    scroll_faucet_url = 'https://prealpha.scroll.io/faucet/'
    scroll_L1_url = 'https://prealpha.scroll.io/bridge/'
    scroll_L2_url = 'https://prealpha.scroll.io/swap/#/'
    scroll_l2_liquidity_url = 'https://prealpha.scroll.io/swap/#/pool'
    scroll_metamask_login = "//p[text()='MetaMask']"
    metamask_nextButton = '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]'
    metamask_loginButton = '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'
    L1_metamask_login = "//span[text()='MetaMask']"
    L2_select_token = "//span[text()='Select a token']"
    faucet_button_xpath = "//button[text()='Request']"
    L1_network = 'Scroll L1 '
    L2_network = 'Scroll L2'
    L1_input_xpath = '//*[@id="root"]/div/div[4]/div[2]/div[1]/div[1]/div[1]/div/input'
    L2_input_xpath = "//input[@class='sc-eerKOB kDGsRH']"
    L2_input_TSETH = "//input[@inputmode='decimal']"
    L2_input_TSUSDC = "(//input[@inputmode='decimal'])[2]"
    L2_swapButton = "//div[text()='Swap']"
    L2_liquidity_button = "//div[text()='Add Liquidity']"
    L2_supply_button = "//div[text()='Supply']"
    L2_confirm_supply = "//div[text()='Confirm Supply']"
    L2_confirmButton = "(//div[text()='Confirm Swap'])[2]"
    L1_sendButton_xpath = '//*[@id="root"]/div/div[4]/div[2]/div[4]/button'
    L2_bridge_input = "//input[contains(@class,'MuiInputBase-input MuiInput-input')]"

    def __init__(self, driver):
        self.driver = actionsBase(driver)

    def scroll_task(self):

        # 打开scroll领水的页面
        self.driver.browser.navi_to_page(self.scroll_faucet_url)
        time.sleep(5)
        # 如果需要登录则登录
        try:
            self.driver.element.click(self.scroll_metamask_login)
            time.sleep(5)
            self.driver.browser.windows_toggle(1)
            self.driver.element.click(self.metamask_nextButton)
            self.driver.element.click(self.metamask_loginButton)
            self.driver.browser.windows_handles()
        except BaseException:
            pass
        # 点击领水按钮
        self.driver.element.click(self.faucet_button_xpath)
        time.sleep(5)
        # metamask切换到L1网络
        self.network_toggle(self.L1_network)
        # 打开L1网页，执行L1--->L2的跨链操作
        self.driver.browser.navi_to_page(self.scroll_L1_url)
        time.sleep(5)
        # 如果需要登录则登录
        try:
            self.driver.element.click(self.L1_metamask_login)
        except BaseException:
            pass
        # 输入需要跨链的token数量
        self.driver.element.send_keys(self.L1_input_xpath, '0.8')
        time.sleep(3)
        # 点击执行跨链操作
        self.driver.element.click(self.L1_sendButton_xpath)
        time.sleep(5)
        # metamask钱包确认操作
        self.metamask_click()

        # metamask切换到L2网络
        self.network_toggle(self.L2_network)
        # 打开L2页面
        self.driver.browser.navi_to_page(self.scroll_L2_url)
        time.sleep(5)
        # 点击选择TSUSDC进行SWAP操作
        self.driver.element.click(self.L2_select_token)
        self.driver.element.send_keys(self.L2_input_xpath, 'TSUSDC')
        self.driver.mouse.keyboard_element(Keys.ENTER)
        time.sleep(3)
        # 输入TSETH的数量进行SWAP操作
        self.driver.element.send_keys(self.L2_input_TSETH, '0.4')
        time.sleep(3)
        # 点击两次按钮进行SWAP操作
        self.driver.element.click(self.L2_swapButton)
        self.driver.element.click(self.L2_confirmButton)
        time.sleep(8)
        # metamask钱包确认操作
        self.metamask_click()
        # 打开L2添加流动性页面
        self.driver.browser.navi_to_page(self.scroll_l2_liquidity_url)
        time.sleep(5)
        # 点击添加流动性按钮
        self.driver.element.click(self.L2_liquidity_button)
        # 点击选择TSUSDC进行添加流动性
        self.driver.element.click(self.L2_select_token)
        self.driver.element.send_keys(self.L2_input_xpath, 'TSUSDC')
        self.driver.mouse.keyboard_element(Keys.ENTER)
        # 输入TSUSDC的数量
        self.driver.element.send_keys(self.L2_input_TSUSDC, '400')
        time.sleep(5)
        # 点击两次按钮确认添加流动性操作
        self.driver.element.click(self.L2_supply_button)
        self.driver.element.click(self.L2_confirm_supply)
        time.sleep(5)
        # metamask钱包确认操作
        self.metamask_click()
        time.sleep(3)
        # 打开跨链页面进行L2--->L1的跨链操作
        self.driver.browser.navi_to_page(self.scroll_L1_url)
        # 输入需要跨链的token数量
        self.driver.element.send_keys(self.L2_bridge_input, '0.1')
        # 点击执行跨链操作
        self.driver.element.click(self.L1_sendButton_xpath)
        time.sleep(5)
        # metamask钱包确认操作
        self.metamask_click()

    def network_toggle(self, value):
        self.driver.browser.navi_to_page("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
        self.driver.element.click('//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span')
        self.driver.element.find_location('network-name-item', value)

    def metamask_click(self):
        self.driver.browser.windows_toggle(1)
        x = 0
        while x <= 5:
            try:
                time.sleep(1)
                self.driver.element.click('//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[2]')
            except BaseException:
                break
            x = x + 1
        # 跳转到浏览器第一个页面
        self.driver.browser.windows_handles()
