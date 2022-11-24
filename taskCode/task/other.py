import random
import time
from taskCode.actions import actionsBase
from taskCode.config.carvURL import carvUrl
from taskCode.actions.textFile import textFile
from .wallet import Wallet


class Other:

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)

    # CARV互关
    def carvFollow(self, adsNum):
        for i in range(len(carvUrl)):
            url = carvUrl[i]
            self.driver.browser.navi_to_page(url)
            time.sleep(5)
            try:
                follow = "//button[contains(@class,'daisy-btn daisy-btn-outline')]"
                self.driver.element.click(follow)
                time.sleep(5)
                notion = self.driver.element.get_text(follow)
                print(adsNum, notion)
            except BaseException:
                pass

    # AVAX测试币领水
    def AVAXFaucet(self, adsNum, acAddress):
        self.driver.browser.navi_to_page('https://faucet.avax.network/')
        time.sleep(5)
        self.driver.element.send_keys('//*[@id="root"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/input', acAddress)
        time.sleep(3)
        self.driver.element.click("//span[text()='Request ']")
        time.sleep(3)
        try:
            self.driver.element.get_text("//button[text()='Back']")
        except BaseException:
            print(adsNum)
            pass

    # FlowCarbon填表有机会获得白名单
    def FlowCarbon(self, adsAddress, adsMail, adsName):
        firstName = adsName.split(" ")[0]
        lastName = adsName.split(" ")[1]
        self.driver.browser.navi_to_page('https://kpkwft1hn0b.typeform.com/to/oCIuiF4a')
        time.sleep(5)
        self.driver.element.click("//button[@data-qa='start-button']")
        time.sleep(2)
        self.driver.element.send_keys("//input[@name='name']", firstName)
        time.sleep(1)
        self.driver.element.click("//button[@data-qa='ok-button-visible deep-purple-ok-button-visible']")
        time.sleep(2)
        self.driver.element.send_keys("(//input[@name='name'])[2]", lastName)
        time.sleep(1)
        self.driver.element.click("(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
        time.sleep(2)
        self.driver.element.send_keys("(//input[@name='name'])[2]", adsAddress)
        time.sleep(1)
        self.driver.element.click("(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
        time.sleep(2)
        self.driver.element.send_keys("//input[@type='email']", adsMail)
        time.sleep(1)
        self.driver.element.click("//button[@data-qa='submit-button deep-purple-submit-button']")
        time.sleep(3)

    # Araya Finance测试网交互任务
    def Araya(self, adsNum, password):
        self.driver.browser.close()
        time.sleep(1)
        self.driver.browser.windows_handles()
        self.driver.browser.close()
        self.driver.browser.windows_handles()
        self.driver.browser.navi_to_page('chrome-extension://pdnijfffcmngbdnhdldgbndpggomemcn/ui.html')
        time.sleep(2)
        self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
        time.sleep(2)
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        time.sleep(3)
        try:
            self.driver.element.clicks('//*[@id="root"]/div/div/div[2]/main/div/div[4]/button')
            time.sleep(10)
        except BaseException:
            pass
        self.driver.browser.navi_to_page('https://www.arayafi.org/swap')
        time.sleep(5)
        try:
            self.driver.element.click("//label[@for='wallet-modal']")
            time.sleep(2)
            self.driver.element.click("//span[text()='Sui Wallet']")
            time.sleep(2)
            self.wallet.suiWallet()
        except BaseException:
            pass
        self.driver.find.xpath_notelement_60sec("//div[contains(@class,'modal-box flex')]")
        self.driver.element.click("//label[text()='Claim test tokens']")
        self.driver.element.click("//li[contains(@class,'h-12 w-30')]//a")
        self.wallet.suiWallet()
        self.driver.find.xpath_notelement_60sec("//div[contains(@class,'modal-box flex')]")
        self.driver.element.click("//label[text()='Claim test tokens']")
        self.driver.element.click("(//li[contains(@class,'h-12 w-30')]//a)[2]")
        self.wallet.suiWallet()
        self.driver.find.xpath_notelement_60sec("//div[contains(@class,'modal-box flex')]")
        self.driver.element.click("//label[text()='Claim test tokens']")
        self.driver.element.click("(//li[contains(@class,'h-12 w-30')]//a)[3]")
        self.wallet.suiWallet()
        self.driver.find.xpath_notelement_60sec("//div[contains(@class,'modal-box flex')]")
        self.driver.element.click("//label[text()='Claim test tokens']")
        self.driver.element.click("//div[@id='__next']/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
        self.wallet.suiWallet()
        print(adsNum, "测试币领取成功")
        self.driver.find.xpath_notelement_60sec("//div[contains(@class,'modal-box flex')]")
        self.driver.element.send_keys("//input[@dir='ltr']", '400')
        time.sleep(2)
        self.driver.element.click("//div[contains(@class,'flex ara-button')]")
        time.sleep(2)
        self.driver.element.click("//div[text()='Confirm']")
        self.wallet.suiWallet()
        self.driver.find.xpath_notelement_60sec("(//div[contains(@class,'modal-box flex')])[2]")
        print(adsNum, "swap成功")
        time.sleep(5)
        self.driver.element.click("//a[@href='/liquidity']")
        time.sleep(8)
        self.driver.element.click("//div[text()='Add Liquidity']")
        time.sleep(2)
        self.driver.element.send_keys("//input[@dir='ltr']", '200')
        time.sleep(2)
        self.driver.element.click("//div[text()='Add Liquidity']")
        self.wallet.suiWallet()
        self.driver.find.xpath_notelement_60sec("(//div[contains(@class,'modal-box flex')])[2]")
        print(adsNum, "流动性添加成功")
        Manage = self.driver.element.get_text_60sec("//div[text()='Manage']")
        self.driver.element.click("//div[text()='Manage']")
        time.sleep(2)
        self.driver.element.click("//div[text()='Remove']")
        time.sleep(2)
        self.driver.element.click("//div[text()='25%']")
        time.sleep(2)
        self.driver.element.click("//div[text()='Remove Liquidity']")
        self.wallet.suiWallet()
        self.driver.find.xpath_notelement_60sec("//div[contains(@class,'modal-box flex')]")
        print(adsNum, "移除流动性成功")

    def suiA(self, x, adsNum, adsName, password):
        self.driver.browser.close_page()
        self.driver.browser.navi_to_page('chrome-extension://iolfjajodolgbdjecfnlbklhicbafeia/ui.html')
        time.sleep(2)
        self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
        time.sleep(2)
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        time.sleep(3)
        try:
            self.driver.element.clicks('//*[@id="root"]/div/div/div[2]/main/div/div[4]/button')
            time.sleep(10)
        except BaseException:
            pass
        self.driver.browser.navi_to_page('https://suia.io/')
        time.sleep(5)
        try:
            self.driver.element.click("//span[text()='Connect Wallet']")
            time.sleep(2)
            self.driver.element.click("//span[text()='Sui Wallet']")
            self.wallet.suiWallet()
        except BaseException:
            pass
        self.driver.element.click("//span[text()='Create Suia']")
        time.sleep(2)
        update = self.driver.find.findX("//input[@type='file']")
        update.send_keys(r'C:\\Users\\chencheng\\PycharmProjects\\mysite\\main\\image\\Square\\' + str(x) + '.png')
        time.sleep(3)
        self.driver.element.send_keys("(//div[@class='form-item']//input)[2]", adsName)
        time.sleep(2)
        self.driver.element.send_keys("//div[@class='form-item']//textarea", adsName)
        time.sleep(2)
        amount = random.randint(655, 9999)
        self.driver.element.send_keys("//input[@type='number']", amount)
        time.sleep(2)
        self.driver.element.click("//div[@class='form-wrapper']//a[1]")
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec("(//div[@role='alert']//div)[2]")
        textFile.write_txt_data(adsNum + notion)
        time.sleep(3)
        try:
            self.driver.element.click('//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/a/a')
            time.sleep(2)
            self.driver.element.click(
                '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div[2]/div/div[2]/div/div/div/button/span')
            self.wallet.suiWallet()
            notion = self.driver.element.get_text_60sec("(//div[@role='alert']//div)")
            textFile.write_txt_data(adsNum + notion)
        except BaseException:
            textFile.write_txt_data(adsNum + "MINT官方失败")
            pass

    # opSide 领水+质押1IDE任务
    def opSide(self, adsNum):
        self.driver.browser.close_page()
        self.wallet.metamask_login(adsNum)
        self.driver.browser.navi_to_page('https://faucet-testnet.opside.network/')
        time.sleep(2)
        self.driver.element.click("//a[contains(@class,'cursor-pointer text-blue-400')]")
        time.sleep(2)
        self.driver.element.click("//button[contains(@class,'w-full flex')]")
        time.sleep(3)
        try:
            self.wallet.metamask_firstSign()
        except BaseException:
            pass
        self.driver.element.click("//button[text()=' Submit ']")
        time.sleep(3)
        self.wallet.metamask_sign()
        notion = self.driver.element.get_text_60sec("//div[@class='el-notification__content']//p[1]")
        textFile.write_txt_data(adsNum + notion)
        time.sleep(3)

        self.driver.browser.navi_to_page('https://staking-testnet.opside.network/')
        time.sleep(2)
        self.driver.element.click("//button[text()='Connect to wallet']")
        time.sleep(2)
        self.driver.element.click("//h3[text()='MetaMask']")
        time.sleep(3)
        self.wallet.metamask_firstSign()
        time.sleep(3)
        self.wallet.metamask_addNetwork()
        time.sleep(2)
        self.driver.element.click("(//button[@type='button'])[2]")
        time.sleep(2)
        self.driver.element.send_keys("//input[contains(@class,'delegate-number border-0')]", "1")
        time.sleep(2)
        self.driver.element.click("//span[text()=' Delegate ']")
        time.sleep(5)
        self.wallet.metamask_submit()
        notion = self.driver.element.get_text_60sec("//h1[contains(@class,'text-black text-lg')]" and "//h1[text()='Delegate Completed']")
        textFile.write_txt_data(adsNum + notion)

    def wizard(self, adsNum, password):
        self.driver.browser.close_page()
        self.driver.browser.navi_to_page('chrome-extension://iolfjajodolgbdjecfnlbklhicbafeia/ui.html')
        time.sleep(2)
        self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
        time.sleep(2)
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        time.sleep(3)
        try:
            self.driver.element.clicks('//*[@id="root"]/div/div/div[2]/main/div/div[4]/button')
            time.sleep(10)
        except BaseException:
            pass
        self.driver.browser.navi_to_page('https://test-wizardland.vercel.app/')
        time.sleep(3)
        self.driver.element.click("//button[text()='Connect Button']")
        time.sleep(2)
        self.driver.element.click("//div[text()='Sui Wallet']")
        time.sleep(2)
        self.wallet.suiWallet()
        time.sleep(3)
        self.driver.element.click("//button[text()='Mint Wizard']")
        time.sleep(3)
        self.wallet.suiWallet()
        notion = self.driver.alert.get_alert_text()
        textFile.write_txt_data(adsNum + notion)

    def gamma_x(self, adsNum, adsMail, adsName, adsAddress, password):
        firstName = adsName.split(" ")[0]
        lastName = adsName.split(" ")[1]
        self.driver.browser.close_page()
        self.driver.browser.navi_to_page('https://gammax.exchange/')
        time.sleep(3)
        self.driver.element.click("//a[@class='btn btn-blue-gradient']")
        time.sleep(5)
        self.driver.wait.hCaptcha_successful()
        self.driver.element.send_keys("//label[text()='First Name']/following::input", firstName)
        time.sleep(2)
        self.driver.element.send_keys("//label[text()='Last Name']/following::input", lastName)
        time.sleep(2)
        self.driver.element.send_keys("//input[@type='email']", adsMail)
        time.sleep(2)
        self.driver.element.send_keys("//label[text()='Metamask Wallet Address']/following::input", adsAddress)
        time.sleep(2)
        self.driver.element.send_keys("//label[text()='Password']/following-sibling::input", password)
        time.sleep(2)
        self.driver.element.click("//button[text()='Sign Up Now!']")
        time.sleep(5)
        notion = self.driver.element.get_text_60sec("//div[contains(@class,'forminator-response-message forminator-show')]//p[1]")
        textFile.write_txt_data(adsNum + notion)
        time.sleep(5)