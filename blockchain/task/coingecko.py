import time
from selenium.webdriver.common.by import By
from blockchain.method import Method
from .wallet import Wallet


class Coingecko:
    def __init__(self, driver):
        self.driver = Method(driver)
        self.wallet = Wallet(driver)

    def coingeckoTask(self, Num, tableName):
        self.driver.browser.navi_to_page('https://www.coingecko.com/account/candy?locale=zh')
        time.sleep(5)
        # attempts = 0
        # while attempts < 3:
        #     attempts += 1
        #     try:
        #         button = self.driver.element.get_button_enabled("(//button[@type='submit'])[2]")
        #         if button:
        #             self.driver.element.click("(//button[@type='submit'])[2]")
        #             time.sleep(5)
        #             notion = self.driver.element.get_text("//div[contains(@class,'col-8 col-lg-10')]//span")
        #             if '小时' not in notion:
        #                 self.driver.mysql.add(tableName, 'CoinGecko', notion, Num)
        #                 break
        #             else:
        #                 self.driver.browser.refresh()
        #                 time.sleep(3)
        #     except BaseException:
        #         next_time = '下次：' + self.driver.element.get_text("(//div[contains(@class,'btn bg-secondary')]//span)[2]")
        #         self.driver.mysql.add(tableName, 'CoinGecko', next_time, Num)
        #         break
        try:
            button = self.driver.element.get_button_enabled_t(By.XPATH, "(//button[@type='submit'])[2]", 3)
            if button:
                self.driver.element.click("(//button[@type='submit'])[2]")
                time.sleep(5)
                self.driver.browser.refresh()
                notion = self.driver.element.get_text("//div[contains(@class,'col-8 col-lg-10')]//span")
                self.driver.mysql.add(tableName, 'CoinGecko', notion, Num)
        except BaseException:
            next_time = '下次：' + self.driver.element.get_text("(//div[contains(@class,'btn bg-secondary')]//span)[2]")
            self.driver.mysql.add(tableName, 'CoinGecko', next_time, Num)

    def cassavaTask(self, Num, tableName):
        # self.driver.browser.maxWindows()
        # self.driver.browser.navi_to_page('https://app.cassava.network/#/myPortal/communities')
        # time.sleep(5)
        # self.driver.element.click("//button[text()='Logout']")
        # self.driver.element.click('//button[@class="btn btn-default btn-small confirmBtn"]')
        self.driver.browser.navi_to_page("https://app.cassava.network/#/")
        time.sleep(3)
        self.driver.browser.refresh()
        time.sleep(3)
        try:
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, "//i[@class='iconfont icon-checkin']", 5)
        except BaseException:
            # self.cassava_login(Num, tableName)
            self.driver.element.click_t(By.XPATH, '//button[@class="btn btn-default btn-small btn-transparent loginBtn"]', 5)
            time.sleep(3)
        self.driver.element.click("//i[@class='iconfont icon-checkin']")
        try:
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, "//div[@class='my-message']//span[@class='text']", 15)
            self.driver.mysql.add(tableName, 'Cassava', '领取成功', Num)
        except BaseException:
            self.driver.mysql.add(tableName, 'Cassava', '失败', Num)

    def cassava_login(self, Num, tableName):
        password = self.driver.config.password_next()
        if tableName == 'ads_task':
            mail = self.driver.config.adsMail(Num)
        else:
            mail = self.driver.config.bitMail(Num)
        try:
            self.driver.element.click_t(By.XPATH, '//button[@class="btn btn-default btn-small btn-transparent loginBtn"]', 3)
            time.sleep(3)
            self.driver.browser.windows_wallet()
            self.driver.element.send_keys_t(By.XPATH, '//input[@placeholder="Please enter your email address"]', mail, 20)
            self.driver.element.click("//span[text()='Log in']")
            self.driver.element.click("//span[text()='Continue with Google']")
            self.driver.element.click_t(By.XPATH, '//div[@class="w1I7fb"]', 60)
            self.driver.element.send_keys_t(By.XPATH, '//input[@placeholder="Please enter password"]', password, 60)
            self.driver.element.click("//span[text()='Log in']")
            self.driver.element.click_t(By.XPATH, "//span[text()='Sign in']", 60)
            time.sleep(5)
            self.driver.browser.windows_handles()
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, "//i[@class='iconfont icon-checkin']", 60)
            time.sleep(3)
        except BaseException:
            self.driver.mysql.add(tableName, 'Cassava', '登录失败', Num)

    def soquestTask(self, Num, tableName):
        self.driver.browser.navi_to_page("https://soquest.xyz/privilege")
        time.sleep(5)
        try:
            self.driver.wait.wait_visibility_of_element_t(By.XPATH, '//*[@alt="notification"]', 5)
        except BaseException:
            buttonText = self.driver.element.get_text('//button[@type="button"]')
            if buttonText == 'Wrong Network':
                self.driver.element.click('//button[@type="button"]')
                self.driver.element.click('//span[text()="Ethereum"]')
                self.wallet.metaMask_SwitchNetWork()
                self.wallet.simple_sign()
            else:
                self.driver.element.click('//button[@type="button"]')
                self.driver.element.click('//span[text()="MetaMask"]')
                self.wallet.simple_sign()
        self.driver.element.click('//div[@class="mui-style-1w0q4w9"]/button')
        time.sleep(2)
        notion = self.driver.element.get_text("//button[text()='Collect Tomorrow']")
        self.driver.mysql.add(tableName, 'Soquest', notion, Num)
        time.sleep(2)

    def CyberConnect(self, Num):
        # self.driver.browser.maxWindows()
        self.driver.browser.navi_to_page('https://atticc.xyz/users/0x414113f5E5D0D34D43c589357739016Ee27adE11/posts/8d42178c-4279-467c-bfbc-0e5f9f4b2720')
        time.sleep(5)
        # self.driver.element.click("//button[text()='Connect Wallet']")
        # self.driver.element.click("//button[text()='MetaMask']")
        # self.wallet.metaMask_Sign()
        # try:
        #     self.wallet.metaMask_Sign()
        # except BaseException:
        #     pass
        # time.sleep(3)
        self.driver.element.click("(//div[contains(@class,'MuiButtonBase-root MuiIconButton-root')])[3]")
        self.driver.element.click("//button[text()='Collect Now']")
        self.wallet.metaMask_Submit()
        time.sleep(3)
        num1 = self.driver.element.get_text_t(By.XPATH, '//span[@class="MuiTypography-root MuiTypography-gradient css-lxzyij"]', 60)
        self.driver.function.write_txt_data(Num + "第一步成功")
        self.driver.browser.navi_to_page('https://link3.to/rektinteractivegg/post/dca1e6e810981e8a7073b98367a0ce3684d98befc3549f6f7c696457aeeb0e7c')
        time.sleep(3)
        self.driver.wait.wait_execute_script_Down()
        self.driver.element.click('//button[@id="mui-2"]')
        self.driver.function.wait_for_text_change('//button[@id="mui-2"]')
        self.driver.function.write_txt_data(Num + "第二步成功")
        self.driver.browser.navi_to_page('https://link3.to/cyberconnect/fanclub')
        time.sleep(3)
        self.driver.element.click("//h4[text()='Like a Post']/../../../button")
        self.driver.function.wait_for_text_change("//h4[text()='Like a Post']/../../../button")
        self.driver.element.click("//h4[text()='Like a Post']/../../../button")
        self.driver.function.wait_for_text_change("//h4[text()='Like a Post']/../../../button")
        self.driver.element.click("//h4[text()='Collect an EssenceNFT']/../../../button")
        self.driver.function.wait_for_text_change("//h4[text()='Collect an EssenceNFT']/../../../button")
        self.driver.function.write_txt_data(Num + "全部成功")
        time.sleep(3)
