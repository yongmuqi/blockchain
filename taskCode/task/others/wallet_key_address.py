import time
from taskCode.actions.textFile import textFile


def Metamask_key_address(self, bitNum, password, x):
    print(x)
    self.wallet.metamask_login(bitNum)
    self.driver.mouse.offset_click_00()
    self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div/div/div[1]/div/div/div/button/div[1]')
    address = textFile.clipboard()
    print(address)
    self.driver.mysql.add_wallet('MatemaskAddress', address, x)
    time.sleep(0.5)
    self.driver.element.click('//*[@id="app-content"]/div/div[1]/div/div[2]/button/div/div')
    time.sleep(0.5)
    self.driver.element.click('//*[@id="app-content"]/div/div[3]/button[5]')
    time.sleep(0.5)
    self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div[2]/div[1]/div/button[4]/div/div[2]')
    time.sleep(0.5)
    self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/button')
    time.sleep(0.5)
    self.driver.element.send_keys('//*[@id="password-box"]', password)
    time.sleep(1)
    self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div[3]/footer/button[2]')
    time.sleep(0.5)
    self.driver.element.click('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div')
    time.sleep(2)
    key = textFile.clipboard()
    print(key)
    self.driver.mysql.add_wallet('Matemask', key, x)
    time.sleep(3)


def Argent_key_address(self, password, x):
    self.driver.browser.navi_to_page('chrome-extension://dlcobpjiigpikoobohmabehhmhfoodbb/index.html')
    time.sleep(2)
    self.driver.element.send_keys("//*[@class='chakra-input css-1eonw3x']", password)
    self.driver.element.click("//button[text()='Unlock']")
    try:
        self.driver.element.click_3sec("//button[text()='I understand']")
    except BaseException:
        pass
    self.driver.element.click('//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div/button')
    address = textFile.clipboard()
    self.driver.mysql.add_wallet('ArgentXAddress', address, x)
    self.driver.element.click('//*[@id="root"]/div/div/div[1]/div[2]/button[2]')
    self.driver.element.click('//*[@id="root"]/div/div/div[2]/div/a[3]/h6')
    self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/div/form/input', password)
    self.driver.element.click("//button[text()='Continue']")
    time.sleep(2)
    self.driver.element.click("//button[text()='Copy']")
    time.sleep(1)
    key = textFile.clipboard()
    self.driver.mysql.add_wallet('ArgentX', key, x)


def sui_key_address(self, password, x):
    self.driver.browser.navi_to_page('chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html')
    time.sleep(2)
    self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
    time.sleep(2)
    self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
    time.sleep(3)
    self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/span/span/i')
    address = textFile.clipboard()
    print(address)
    self.driver.mysql.add_wallet('SuiAddress', address, x)
    time.sleep(3)


def petra_key_address(self, password, x):
    self.driver.browser.navi_to_page('chrome-extension://ejjladinnckdgjemekebdpeokbikhfci/index.html')
    time.sleep(2)
    self.driver.element.send_keys('//*[@id="field-:r1:"]', password)
    time.sleep(1)
    self.driver.element.click("//button[text()='Unlock']")
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[2]/div[1]/div/div/button')
    time.sleep(1)
    address = textFile.clipboard()
    print(address)
    self.driver.mysql.add_wallet('PetraAddress', address, x)
    time.sleep(2)
    self.driver.element.click('//*[@id="root"]/div/div[4]/div/div[4]/a/p')
    time.sleep(0.5)
    self.driver.element.click('//*[@id="root"]/div/div[3]/div[1]/div[4]/div[1]/a/div/div[1]')
    time.sleep(0.5)
    self.driver.element.send_keys('(//*[contains(@id,"field")])[2]', password)
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[3]/div/form/div/div[2]/button')
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[3]/div/div[1]/div/button')
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[3]/div/div[2]/span/button')
    time.sleep(2)
    key = textFile.clipboard()
    print(key)
    self.driver.mysql.add_wallet('Petra', key, x)
    time.sleep(3)


def phantom(self, x):
    self.driver.browser.navi_to_page("chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/popup.html")
    time.sleep(3)
    self.driver.element.send_keys('//input[@type="password"]', '3981786cc')
    time.sleep(1)
    self.driver.element.click('//button[@type="submit"]')
    time.sleep(2)
    try:
        self.driver.element.click_3sec("//button[text()='Close']")
    except BaseException:
        pass
    time.sleep(3)
    self.driver.element.click('//p[@class="sc-hKwDye UoIuP sc-hSvFVY bYZZTT"]')
    time.sleep(1)
    self.driver.element.click('(//button[@type="button"])[4]')
    address = textFile.clipboard()
    self.driver.mysql.add_wallet('PhantomAddress', address, x)
    time.sleep(1)
    self.driver.element.click('//div[@data-testid="settings-menu-close-button"]')
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/section/div[1]/p')
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[2]/p[1]')
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[5]/div/div/div[1]/div/div[3]')
    time.sleep(1)
    self.driver.element.click('//*[@id="root"]/div/div[5]/div/div/div[3]/div[2]/div[1]/p')
    time.sleep(1)
    self.driver.element.send_keys('//input[@type="password"]', '3981786cc')
    time.sleep(1)
    self.driver.element.click('//button[@type="submit"]')
    key_values = []
    # //input[@class="sc-dkqQuH fWCGRo"]
    values = self.driver.find.xpath_elements('//input[@class="sc-dkqQuH fWCGRo"]')
    for v in values:
        key_values.append(v.get_attribute('value'))
    self.driver.mysql.add_wallet('Phantom', str(key_values), x)
    time.sleep(1)
