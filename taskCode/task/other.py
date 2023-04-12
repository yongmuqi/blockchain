import random
import string
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from taskCode.actions import actionsBase, Query
from taskCode.config.carvURL import carvUrl
from taskCode.actions.textFile import textFile
from taskCode.task.reCaptcha import reCaptcha
from taskCode.task.solution import Solution
from taskCode.task.wallet import Wallet


class Other:

    def __init__(self, driver):
        self.driver = actionsBase(driver)
        self.wallet = Wallet(driver)
        self.q = Query()

    def openYesCaptcha(self):
        self.driver.browser.navi_to_page("chrome-extension://jiofmdifioeejeilfkpegipdjiopiekl/popup/index.html")
        time.sleep(2)
        try:
            statue = self.driver.find.xpath_element_3sec('//span[contains(@class, "Mui-checked css-1g3pnk5")]')
        except BaseException:
            self.driver.element.click('//*[@id="app"]/div/div[1]/div[2]/span/span[1]')

    def closeYesCaptcha(self):
        self.driver.browser.navi_to_page("chrome-extension://jiofmdifioeejeilfkpegipdjiopiekl/popup/index.html")
        time.sleep(2)
        try:
            statue = self.driver.find.xpath_element_3sec('//span[contains(@class, "Mui-checked css-1g3pnk5")]')
            self.driver.element.click('//*[@id="app"]/div/div[1]/div[2]/span/span[1]')
        except BaseException:
            pass

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
        self.driver.browser.navi_to_page('https://gammax.exchange/beta-tester/')
        time.sleep(5)
        self.driver.element.send_keys('//input[@name="text-2"]', firstName)
        time.sleep(2)
        self.driver.element.send_keys('//input[@name="text-3"]', lastName)
        time.sleep(2)
        self.driver.element.send_keys("//input[@type='email']", adsMail)
        time.sleep(2)
        select = self.driver.element.find.findX('//select[@name="address-1-country"]')
        se = Select(select)
        se.select_by_value('United States of America (USA)')
        time.sleep(2)
        self.driver.element.send_keys('//input[@name="text-1"]', adsAddress)
        time.sleep(2)
        self.driver.element.send_keys('//input[@name="password-1"]', password)
        time.sleep(2)
        self.driver.wait.wait_execute_script("var q=document.documentElement.scrollTop=100")
        time.sleep(1)
        Solution(self.driver).resolve()
        time.sleep(3)
        self.driver.element.click("//button[text()='Register']")
        time.sleep(5)
        notion = self.driver.element.get_text_60sec("//li[contains(@class,'avatar menu-item')]//a")
        textFile.write_txt_data(adsNum + notion)
        time.sleep(5)

    # shardeum生态交互续集
    def shardeum(self, adsAddress, adsNum):
        # # 领水（$SHM)功能
        # self.driver.browser.navi_to_page('https://faucet.liberty10.shardeum.org/')
        # time.sleep(3)
        # self.driver.wait.hCaptcha_successful('//*[@id="hcap-script"]/iframe')
        # self.driver.element.click("//div[@class='instruction-container']//a[1]")
        # time.sleep(2)
        # self.driver.element.click("//button[text()='Okay']")
        # time.sleep(5)
        # self.driver.browser.windows_toggle(1)
        # time.sleep(5)
        # # 跳转到推特页面
        # for x in range(43):
        #     self.driver.mouse.keyboard_element(Keys.BACKSPACE)
        # self.driver.element.send_keys("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']", adsAddress)
        # time.sleep(3)
        # # self.driver.element.click("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        # # self.driver.mouse.ctrl_a()
        # # text = "I'm excited about the @Shardeum Liberty alphanet! #Shardeum is building an EVM-based L1 that can deliver low gas fees forever by adding more nodes.\n\nRequesting 100 #SHM from the Shardeum faucet. https://faucet.liberty10.shardeum.org/\n\nMy address is: " + adsAddress
        # # self.driver.element.send_keys("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']", text)
        # self.driver.element.click("//div[@data-testid='tweetButton']")
        # time.sleep(5)
        # self.driver.element.click("//a[@data-testid='AppTabBar_Profile_Link']//div")
        # time.sleep(5)
        # self.driver.element.click("//div[@data-testid='tweetText']")
        # time.sleep(5)
        # self.driver.mouse.move_on_element_click('//*[contains(@id,"__")]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]')
        # time.sleep(1)
        # self.driver.element.click("//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]")
        # time.sleep(1)
        # self.driver.browser.windows_handles()
        # self.driver.element.click("//input[@placeholder='Tweet URL containing your address']")
        # self.driver.mouse.ctrl_v()
        # time.sleep(3)
        # self.driver.element.click("//button[@type='submit']")
        # time.sleep(5)
        # notion = self.driver.element.get_text_60sec('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/p')
        # print(notion)
        # textFile.write_txt_data(adsNum + notion)
        # time.sleep(3)

        # 测试网交互
        self.driver.browser.navi_to_page('https://boss.shardeum.us/')
        time.sleep(3)
        self.driver.element.click("//div[@class='header_connect']//button[1]")
        time.sleep(5)
        self.wallet.metamask_firstSign()
        try:
            self.driver.element.click_3sec("//div[@role='alert']")
        except BaseException:
            pass
        self.driver.element.click("//div[@class='minus pumi']")
        time.sleep(1)
        self.driver.element.click("//button[text()='Mint Your NFT']")
        time.sleep(5)
        try:
            self.wallet.metamask_switch()
        except BaseException:
            pass
        time.sleep(5)
        self.wallet.metamask_submit()
        notion = self.driver.element.get_text_60sec("(//div[@class='Toastify__toast-body']//div)[2]")
        textFile.write_txt_data(adsNum + notion)

        self.driver.browser.navi_to_page('https://nft.shardeum.us/')
        time.sleep(3)
        self.driver.element.click("//button[text()='Connect Wallet']")
        time.sleep(5)
        self.wallet.metamask_firstSign()
        # 随机生成7位英文加数字
        count = 7
        lastName = "".join([random.choice(string.ascii_letters + string.digits) for i in range(count)])
        self.driver.element.send_keys("//input[@placeholder='domain']", lastName)
        time.sleep(1)
        self.driver.element.click("//button[text()='Mint']")
        time.sleep(5)
        self.wallet.metamask_submit()
        self.driver.wait.wait_visibility_of_notElement_60sec('//*[@id="root"]/div/div/div[1]/svg')
        textFile.write_txt_data(adsNum + "域名MINT成功")

    # tunego
    def tunego(self, adsName, adsMail):
        self.driver.browser.navi_to_page('https://thanksgiving.tunego.com/?kid=2J9S83')
        time.sleep(5)
        count = 7
        lastName = adsName.split(" ")[1]
        self.driver.element.send_keys("//input[@placeholder='Name']", lastName)
        time.sleep(1)
        self.driver.element.send_keys("//input[@type='email']", adsMail)
        time.sleep(1)
        self.driver.element.click("//button[@type='submit']")
        time.sleep(10)
        self.driver.element.click("//div[@data-kol-editor='button']//a[1]")
        time.sleep(10)
        self.driver.element.click('//*[@id="__next"]/div[1]/div/div/button')
        time.sleep(10)
        self.driver.browser.windows_toggle(1)
        self.driver.element.click('//*[@id="root"]/div/div/div/div/div[1]/form/div[3]/div[2]/div/div[2]')
        time.sleep(10)
        self.driver.element.click('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]')
        time.sleep(10)
        self.driver.browser.windows_handles()
        time.sleep(10)
        self.driver.element.click('//*[@id="__next"]/div[1]/div/div/button')
        time.sleep(10)
        self.driver.browser.windows_toggle(1)
        self.driver.element.click('//*[@id="__next"]/main/div[1]/main/div/div[1]/div/div[4]/button[2]')
        time.sleep(10)
        self.driver.browser.windows_handles()
        notion = self.driver.element.get_text_60sec('//*[@id="id-0yk2irlcx3w"]')
        print(notion)

    # 蓝精灵 邮箱填写订阅
    def thesmurfssociety(self, adsNum, adsMail):
        self.driver.browser.navi_to_page('https://thesmurfssociety.com/')
        time.sleep(5)
        for i in range(9):
            self.driver.mouse.keyboard_element(Keys.SPACE)
            time.sleep(3)
        self.driver.element.send_keys("//input[@type='email']", adsMail)
        time.sleep(1)
        self.driver.element.click("//button[@type='submit']")
        time.sleep(2)
        notion = self.driver.element.get_text("//div[contains(@class,'form__feedback active')]")
        textFile.write_txt_data(adsNum + notion)

    #
    def tsunami(self, adsNum, adsDiscord):
        self.driver.browser.navi_to_page('https://tsunami.finance/trade')
        time.sleep(5)
        self.driver.element.click("//div[text()='Connect']")
        time.sleep(1)
        self.driver.element.click("//label[text()='Petra']")
        time.sleep(3)
        # try:
        #     self.wallet.petraWallet()
        # except BaseException:
        #     pass
        # try:
        #     # 验证推特
        #     self.driver.element.click_3sec("//button[text()='Tweet!']")
        #     time.sleep(3)
        #     self.driver.browser.windows_toggle(1)
        #     time.sleep(5)
        #     self.driver.element.click("//div[@data-testid='tweetButton']")
        #     time.sleep(5)
        #     self.driver.browser.close()
        #     self.driver.browser.windows_handles()
        #     self.driver.wait.wait_visibility_of_notElement_60sec("//button[text()='Tweet!']")
        #     time.sleep(3)
        # except BaseException:
        #     pass
        #
        # 领取测试币
        # try:
        #     self.driver.element.click("//div[@class='flex items-center']/following-sibling::button")
        #     self.wallet.petraWallet()
        #
        #     self.driver.element.while_button_60sec("(//div[@class='flex items-center']/following-sibling::button)[2]")
        #     self.wallet.petraWallet()
        #
        #     self.driver.element.while_button_60sec("(//div[@class='flex items-center']/following-sibling::button)[3]")
        #     self.wallet.petraWallet()
        #
        #     self.driver.element.while_button_60sec("//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/button[1]")
        #     self.wallet.petraWallet()
        # except BaseException:
        #     textFile.write_txt_data(adsNum + "领取测试币失败")
        # SWAP10次，并超过5WU
        self.driver.element.click("//div[text()='BTC']")
        time.sleep(1)
        self.driver.element.click("//label[text()='Tether']")
        time.sleep(2)
        self.driver.element.send_keys("//input[@placeholder='0']", '1900')
        for x in range(8):
            self.driver.element.while_button_60sec("//button[text()='Swap']")
            self.wallet.petraWallet()
            time.sleep(5)
        time.sleep(10)
        for x in range(2):
            self.driver.element.click("//img[contains(@class,'h-8 m-[-12px]')]")
            time.sleep(10)
            self.driver.element.click("//button[text()='MAX']")
            self.driver.element.while_button_60sec("//button[text()='Swap']")
            self.wallet.petraWallet()
            time.sleep(3)
            self.driver.wait.wait_visibility_of_notElement_60sec("//td[text()='Swap']")
            time.sleep(5)
        time.sleep(5)
        # 添加流动性10次
        self.driver.element.click("//span[@href='/pool']")
        time.sleep(5)
        self.driver.element.click("//div[text()='BTC']")
        time.sleep(1)
        self.driver.element.click("//label[text()='USD Coin']")
        time.sleep(8)
        self.driver.element.send_keys("//input[@placeholder='0']", '300')
        for x in range(10):
            self.driver.element.while_button_60sec("//button[text()='Provide Liquidity']")
            self.wallet.petraWallet()
            time.sleep(3)
        time.sleep(20)
        # 移除流动性5次
        self.driver.element.click("//div[text()='Withdraw']")
        time.sleep(3)
        self.driver.element.send_keys("//input[@placeholder='0']", '10')
        time.sleep(3)
        for x in range(5):
            self.driver.element.while_button_60sec("//button[text()='Withdraw Liquidity']")
            self.wallet.petraWallet()
            time.sleep(3)
        time.sleep(3)
        self.driver.element.click('//*[@id="__next"]/div/nav/div/div[2]/button[1]')
        time.sleep(1)
        notion = self.driver.element.get_text_60sec("(//div[contains(@class,'text-xs bg-odyssey-black')])[2]")
        self.driver.element.send_keys("//input[contains(@class,'rounded-lg p-3')]", adsDiscord)
        time.sleep(1)
        self.driver.element.click('//*[@id="__next"]/div/div[4]/div/div[2]/div/div/div[6]/button')
        time.sleep(10)
        textFile.write_txt_data(adsNum + "成功")

    # BNB领水
    def bnb_Faucet(self, absNum, absAddress):
        mainXpath = '//iframe[contains(@src, "checkbox")]'
        imageXpath = '//iframe[contains(@src, "challenge")]'
        self.driver.browser.navi_to_page('https://testnet.bnbchain.org/faucet-smart')
        time.sleep(5)
        Solution(self.driver).resolve()
        time.sleep(2)
        self.driver.element.click('//*[@id="url"]')
        time.sleep(1)
        self.driver.element.send_keys('//*[@id="url"]', absAddress)
        time.sleep(1)
        self.driver.element.click("//button[@data-toggle='dropdown']")
        time.sleep(1)
        self.driver.element.click('//*[@id="contendBody"]/div/div[2]/div/div/span[1]/ul/li/a')
        time.sleep(3)
        notion = self.driver.element.get_text("//div[@class='noty_message']//span[1]")
        print(absNum + notion)

    def starkNet_Faucet(self):
        self.driver.browser.navi_to_page('https://faucet.goerli.starknet.io/#')
        time.sleep(5)
        reCaptcha(self.driver).resolve()
        time.sleep(10)

    def claimyoursoul(self, adsNum):
        self.driver.browser.navi_to_page('https://beta.claimyoursoul.masa.finance/')
        time.sleep(5)
        try:
            self.driver.element.click_3sec("//span[text()='Connect wallet']")
            time.sleep(2)
            self.driver.element.click('//*[@id="connect-metamask"]/p')
            time.sleep(5)
            self.wallet.metamask_firstSign()
            try:
                self.wallet.metamask_switch()
            except BaseException:
                pass
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec("//span[text()='Switch to ']")
            time.sleep(5)
            self.wallet.metamask_switch()
        except BaseException:
            pass
        try:
            self.driver.element.click_3sec('//*[@id="authenticate"]')
            time.sleep(5)
            self.wallet.metamask_sign()
        except BaseException:
            pass
        try:
            self.driver.element.click("//h1[text()='Soul names']")
        except BaseException:
            aa = self.driver.element.get_text_60sec("//span[text()='Create identity']")
            self.driver.element.click("//span[text()='Create identity']")
            time.sleep(2)
            self.driver.element.click("//span[text()='Get started']")
        # 随机生成4位英文加数字
        count = 4
        SoulName = "".join([random.choice(string.ascii_letters + string.digits) for i in range(count)])
        self.driver.element.clear("//input[contains(@class,'px-4 py-3')]")
        self.driver.element.send_keys("//input[contains(@class,'px-4 py-3')]", SoulName)
        time.sleep(3)
        self.driver.element.click("//p[text()='Claim your soul']")
        time.sleep(15)
        self.wallet.metamask_submit()
        notion = self.driver.element.get_text_60sec("//h1[contains(@class,'text-center font-regular')]")
        textFile.write_txt_data(adsNum + notion)
        try:
            self.driver.element.click("//span[text()='Go to dashboard']")
            time.sleep(2)
        except BaseException:
            aa = self.driver.element.get_text_60sec("//h1[text()='Credit score']")
        self.driver.element.click("//h1[text()='Credit score']")
        time.sleep(3)
        self.driver.element.click("//h1[text()='DeFi credit score']")
        time.sleep(2)
        self.driver.element.click("//span[text()='Mint score']")
        time.sleep(5)
        try:
            tryAgain = self.driver.element.get_text("//span[text()='Try again']")
            self.q.add('OtherTask1', 'soul最后一步没完成', adsNum)
        except BaseException:
            self.wallet.metamask_submit()
            nextNotion = self.driver.element.get_text_60sec("//span[text()='Continue']")
            self.driver.element.click("//span[text()='Continue']")
            self.q.add('OtherTask1', 'soul任务成功', adsNum)
        time.sleep(5)

    def starkSwap(self, Num, password):
        self.driver.browser.navi_to_page('chrome-extension://dlcobpjiigpikoobohmabehhmhfoodbb/index.html')
        time.sleep(3)
        self.driver.element.send_keys("//*[@class='chakra-input css-1eonw3x']", password)
        self.driver.element.click("//button[text()='Unlock']")
        time.sleep(2)
        self.driver.browser.navi_to_page('https://www.starkswap.co/app/faucet')
        time.sleep(5)
        self.driver.element.click("//button[text()='Connect Wallet']")
        time.sleep(5)
        try:
            self.wallet.argentX_Sign()
        except BaseException:
            pass
        self.driver.element.click("//button[text()='Select a token']")
        time.sleep(1)
        self.driver.element.click("//span[text()='LAN']")
        time.sleep(1)
        self.driver.element.click("//button[text()='+ Add Token']")
        time.sleep(1)
        self.driver.element.clear("//input[@inputmode='decimal']")
        self.driver.element.send_keys("//input[@inputmode='decimal']", "100")
        self.driver.element.clear("(//input[@inputmode='decimal'])[2]")
        self.driver.element.send_keys("(//input[@inputmode='decimal'])[2]", "100")
        time.sleep(1)
        self.driver.element.click("//button[text()='Mint']")
        time.sleep(5)
        self.wallet.argentX_Wallet()
        notion = self.driver.element.get_text_60sec("//p[contains(@class,'MuiTypography-root MuiTypography-body2')]")
        textFile.write_txt_data(Num + notion)
        self.driver.element.click("//button[text()='Go Back']")
        time.sleep(2)
        self.driver.element.click("//div[@role='tablist']//button[1]")
        time.sleep(2)
        self.driver.element.click("//div[@class='MuiBox-root css-18d2quh']//div")
        time.sleep(1)
        self.driver.element.click("//span[text()='BAR']")
        time.sleep(1)
        self.driver.element.click("//button[text()='Select a token']")
        time.sleep(1)
        self.driver.element.click("//span[text()='LAN']")
        time.sleep(1)
        self.driver.element.send_keys("//input[@inputmode='decimal']", "50")
        time.sleep(2)
        self.driver.element.click("(//button[text()='Swap'])[2]")
        time.sleep(2)
        self.driver.element.click("//button[text()='Confirm Swap']")
        time.sleep(5)
        self.wallet.argentX_Wallet()
        notion = self.driver.element.get_text_60sec("//p[contains(@class,'MuiTypography-root MuiTypography-body2')]")
        textFile.write_txt_data(Num + notion)
        self.driver.element.click("//button[text()='Go Back']")
        time.sleep(2)
        self.driver.element.click("//button[text()='Pool']")
        time.sleep(1)
        self.driver.element.click("//p[text()='LAN-BAR']")
        time.sleep(1)
        self.driver.element.send_keys("//input[@inputmode='decimal']", "30")
        time.sleep(1)
        self.driver.element.click("(//button[text()='Deposit'])[2]")
        time.sleep(1)
        self.driver.element.click("//button[text()='Confirm Deposit']")
        time.sleep(5)
        self.wallet.argentX_Wallet()
        notion = self.driver.element.get_text_60sec("//p[contains(@class,'MuiTypography-root MuiTypography-body2')]")
        textFile.write_txt_data(Num + notion)
        self.driver.element.click("//button[text()='Go Back']")
        time.sleep(2)
        self.driver.element.click("//button[text()='Withdraw']")
        time.sleep(1)
        self.driver.element.send_keys("//input[@inputmode='decimal']", "5")
        time.sleep(1)
        self.driver.element.click("(//button[text()='Withdraw'])[2]")
        time.sleep(2)
        self.driver.element.click("//button[text()='Confirm Withdraw']")
        time.sleep(5)
        self.wallet.argentX_Wallet()
        notion = self.driver.element.get_text_60sec("//p[contains(@class,'MuiTypography-root MuiTypography-body2')]")
        textFile.write_txt_data(Num + notion)
        self.driver.element.click("//button[text()='Go Back']")
        time.sleep(2)


        # 融资8000万美金 - 模块化公链Fuel介绍及测试交互教程
    def fuel(self, bitNum, password, x):
        # self.driver.browser.windows_handles()
        # textFile.write_txt_data("------" + bitNum + "开始------")
        # self.driver.browser.navi_to_page(
        #     'chrome-extension://imhekmjjmjhlhlokhaabckaiiblmgpgf/index.html#/sign-up/welcome')
        # try:
        #     self.driver.element.click_3sec("//button[text()='Create a Wallet']")
        # except BaseException:
        #     pass
        # try:
        #     self.driver.element.click("//button[text()='Copy']")
        #     time.sleep(2)
        #     key = textFile.clipboard()
        #     print(key)
        #     self.driver.mysql.add_wallet('Fuel', key, x)
        #     self.driver.element.click('//*[@id="confirmSaved"]')
        #     time.sleep(1)
        #     self.driver.element.click("//button[text()='Next']")
        #     time.sleep(1)
        #     self.driver.element.click('//*[@id="root"]/main/div/div[3]/div/div/div[1]/div/input')
        #     # 接受弹窗
        #     time.sleep(2)
        #     self.driver.mouse.ctrl_v()
        #     time.sleep(1)
        #     self.driver.element.click("//button[text()='Next']")
        #     time.sleep(1)
        #     self.driver.element.send_keys('//*[@id=":r1:"]', password)
        #     time.sleep(1)
        #     self.driver.element.send_keys('//*[@id=":r3:"]', password)
        #     time.sleep(1)
        #     self.driver.element.click('//*[@id=":r5:"]')
        #     self.driver.element.click("//button[text()='Next']")
        #     time.sleep(3)
        #     self.driver.browser.navi_to_page('chrome-extension://imhekmjjmjhlhlokhaabckaiiblmgpgf/popup.html')
        #     time.sleep(3)
        #     self.driver.element.click(
        #         '//*[@id="root"]/main/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/button/span')
        #     time.sleep(1)
        #     address = textFile.clipboard()
        #     print(address)
        #     self.driver.mysql.add_wallet('FuelAddress', address, x)
        #     time.sleep(2)
        # except BaseException:
        #     textFile.write_txt_data(bitNum + "钱包创建失败或已创建过")
        #     pass
        try:
            self.openYesCaptcha()
            self.driver.browser.navi_to_page('chrome-extension://imhekmjjmjhlhlokhaabckaiiblmgpgf/popup.html')
            time.sleep(3)
            self.driver.element.click("//button[text()='Faucet']")
            self.driver.browser.windows_toggle(1)
            self.driver.wait.reCaptcha_successful()
            self.driver.element.click('//input[@type="submit"]')
            time.sleep(15)
            self.driver.browser.close()
            time.sleep(3)
            self.driver.browser.windows_handles()
        except BaseException:
            textFile.write_txt_data(bitNum + "领水失败")
            pass
        # try:
        #     self.driver.browser.navi_to_page('https://fuels-wallet.vercel.app/docs/how-to-use/')
        #     time.sleep(3)
        #     self.driver.element.click("//button[text()='Connect']")
        #     time.sleep(3)
        #     try:
        #         self.wallet.fuel_wallet()
        #     except BaseException:
        #         pass
        #     self.driver.element.click("//button[text()='Get accounts']")
        #     time.sleep(3)
        #     self.driver.wait.wait_execute_script_Down()
        #     time.sleep(1)
        #     self.driver.element.click("//button[text()='Sign Message']")
        #     time.sleep(3)
        #     self.wallet.fuel_wallet_sign()
        #     self.driver.element.click("//button[text()='Transfer']")
        #     time.sleep(8)
        #     self.wallet.fuel_wallet_Confirm()
        # except BaseException:
        #     textFile.write_txt_data(bitNum + "交互失败")
        #     pass

        # self.driver.browser.navi_to_page('https://fuellabs.github.io/swayswap/welcome/create-wallet')
        # self.driver.element.click("//button[text()='Create Wallet']")
        # self.driver.wait.reCaptcha_successful()
        # self.driver.element.while_button_60sec("//button[text()='Give me ETH']")
        # try:
        #     self.driver.find.xpath_element('//*[@id="root"]/div[1]/div/div/div/div[2]')
        #     self.driver.browser.refresh()
        #     self.driver.wait.reCaptcha_successful()
        #     self.driver.element.while_button_60sec("//button[text()='Give me ETH']")
        # except BaseException:
        #     pass
        # notion = self.driver.element.get_text_60sec("//div[@class='welcomeStep']//h2[1]")
        #
        # self.driver.element.click("//input[@type='checkbox']")
        # self.driver.element.click("//button[text()='Get Swapping!']")
        # self.driver.element.send_keys("//input[@inputmode='decimal']", '0.3')
        # self.driver.element.click("//div[text()='Select token']")
        # self.driver.element.click("(//div[text()='DAI'])[2]")
        # self.driver.element.while_button_60sec("(//button[text()='Swap'])[2]")
        # notion = self.driver.element.get_text_60sec("//div[@role='status']")
        #
        # self.driver.element.click("//button[text()='Pool']")
        # self.driver.element.click("//button[text()='Add Liquidity']")
        # self.driver.element.send_keys("//input[@inputmode='decimal']", '0.05')
        # self.driver.element.send_keys('//*[@id="coinTo"]', '100')
        # self.driver.element.while_button_60sec("//button[text()='Create liquidity']")
        # notion = self.driver.element.get_text_60sec("//div[@role='status']")

        # self.closeYesCaptcha()

    def phantom(self, x):
        self.driver.browser.navi_to_page("chrome-extension://ecmicpdpajdjebbckaghpdhinfcpcpaf/popup.html")
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

    def cent(self, adsMail):
        self.driver.browser.navi_to_page("https://thecollectbutton.com/#JoinIn")
        time.sleep(5)
        self.driver.element.click("//a[@class='collectBtn thick']")
        time.sleep(2)
        self.driver.wait.wait_execute_script("var q=document.documentElement.scrollTop=1000")
        time.sleep(2)
        self.driver.element.click('//div[@class="collect-button"]')
        time.sleep(2)
        self.driver.element.send_keys('//*[@id="email-input"]', adsMail)

    def p00ls(self, adsNum):
        self.driver.browser.navi_to_page("https://launchpad.p00ls.io/auth/signin?return_to=%2Fprive")
        time.sleep(5)
        try:
            self.driver.element.click("//div[text()='Login with Google']")
            time.sleep(5)
            self.driver.browser.windows_toggle(1)
            self.driver.element.click('//div[@class="w1I7fb"]')
            time.sleep(5)
            self.driver.browser.windows_handles()
            notion = self.driver.element.get_text_60sec('//span[@class="neueBit text-base tracking-widest"]')
        except BaseException:
            pass
        self.driver.browser.windows_handles()
        try:
            self.driver.element.click("//div[text()='Login with Google']")
            time.sleep(5)
        except BaseException:
            pass
        self.driver.browser.navi_to_page("https://launchpad.p00ls.io/prive/d/d7o5C3ttfA03sJJTyEY0")
        time.sleep(5)
        self.driver.element.click("//button[text()='Take the quiz']")
        time.sleep(1)
        self.driver.element.click("//div[text()='The 2020 Summer Olympics in Tokyo, Japan ']")
        time.sleep(1)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(1)
        self.driver.element.click("//div[text()='LayBack Beer']")
        time.sleep(1)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(1)
        self.driver.element.click("//div[text()='2008']")
        time.sleep(1)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(1)
        notion = self.driver.element.get_text_60sec("//div[@class='m-auto text-center']//div[1]")
        textFile.write_txt_data(adsNum + notion)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(2)

        self.driver.element.click("//button[text()='Learn']")
        time.sleep(1)
        self.driver.element.click("//button[@type='submit']")
        time.sleep(1)
        self.driver.element.click("//div[text()='Florianópolis']")
        time.sleep(1)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(1)
        self.driver.element.click("//div[text()='6']")
        time.sleep(1)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(1)
        self.driver.element.click("//div[text()='Privê']")
        time.sleep(1)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(1)
        notion = self.driver.element.get_text_60sec("//div[@class='m-auto text-center']//div[1]")
        textFile.write_txt_data(adsNum + notion)
        self.driver.element.click("//button[text()='continue']")
        time.sleep(2)

        # self.driver.element.click("//button[text()='Watch']")
        # time.sleep(5)
        # self.driver.wait.wait_switch_to_frame('//iframe[@title="PRIVÊ® MANIFESTO S27"]')
        # time.sleep(1)
        # self.driver.element.click('//button[@class="ytp-large-play-button ytp-button ytp-large-play-button-red-bg"]')
        # time.sleep(1)
        # self.driver.wait.wait_switch_to_default()
        # time.sleep(1)
        # self.driver.element.while_button_60sec("//button[text()='continue']")
        # time.sleep(1)
        # self.driver.element.click("//div[text()='Togetherness, being with each other, in every corner and eternal movement. ']")
        # time.sleep(1)
        # self.driver.element.click("//button[text()='continue']")
        # time.sleep(1)
        # notion = self.driver.element.get_text_60sec("//div[@class='m-auto text-center']//div[1]")
        # textFile.write_txt_data(adsNum + notion)
        # self.driver.element.click("//button[text()='continue']")
        # time.sleep(2)

    def mirmglobal(self, adsMail, adsNum):
        self.openYesCaptcha()
        self.driver.browser.navi_to_page("https://mirmglobal.com/preregistration")
        time.sleep(5)
        try:
            self.driver.element.click("//button[text()='Allow all cookies']")
        except BaseException:
            pass
        time.sleep(3)
        self.driver.element.click('//button[@class="btn-register"]')
        time.sleep(3)
        self.driver.element.send_keys('//input[@type="email"]', adsMail)
        time.sleep(1)
        self.driver.element.click("//div[@class='agree-area']//label[1]")
        time.sleep(1)
        self.driver.element.click("//div[@class='agree-area']//label[2]")
        time.sleep(1)
        self.driver.element.click("//button[text()='PRE-REGISTER']")
        time.sleep(5)
        # self.driver.wait.reCaptcha_successful()
        notion = self.driver.element.get_text_60sec('//div[@class="message"]')
        self.driver.browser.navi_to_page("https://mail.google.com/mail/u/0/#inbox")
        time.sleep(10)
        email = self.driver.element.get_text_60sec('//span[@email="support@mirmglobal.com"]')
        self.driver.element.click("(//span[@class='zF'])[2]")
        time.sleep(2)
        self.driver.wait.wait_visibility_of_element_LINK_TEXT("Verify")
        self.driver.browser.windows_toggle(1)
        mes = self.driver.element.get_text_60sec("//div[@class='modal-alert']//div[1]")
        print(adsNum + mes)
        self.closeYesCaptcha()

    def zelta(self, adsMail, adsAddress, adsNum):
        self.driver.browser.navi_to_page("https://zelta.io/")
        time.sleep(5)
        self.driver.element.click("//button[text()='Claim MY FREE NFT']")
        time.sleep(1)
        self.driver.element.send_keys('//input[@class="chakra-input mb-2 css-1xdt7mp"]', adsMail)
        time.sleep(1)
        self.driver.element.send_keys("//input[@name='address']", adsAddress)
        time.sleep(1)
        self.driver.element.click("//button[text()='Claim Now']")
        notion = self.driver.element.get_text_60sec('//h1[@class="mb-2"]')
        textFile.write_txt_data(adsNum + notion)

    def suia_mint(self, password, adsNum):
        self.driver.browser.navi_to_page('chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html')
        time.sleep(2)
        self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
        time.sleep(2)
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        time.sleep(3)
        try:
            self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/div[4]/button')
            time.sleep(10)
            mes = self.driver.element.get_text_60sec("(//span[text()='0.05'])[2]")
        except BaseException:
            pass
        self.driver.browser.navi_to_page('https://suia.io/home/brands')
        time.sleep(5)
        try:
            self.wallet.suiWallet()
        except BaseException:
            pass
        try:
            self.driver.element.click("//span[text()='Connect Wallet']")
            time.sleep(2)
            self.driver.element.click("//span[text()='Sui Wallet']")
            self.wallet.suiWallet()
        except BaseException:
            pass
        try:
            self.driver.browser.navi_to_page('https://suia.io/brands/OmniBTC')
            time.sleep(5)
            self.driver.element.click('//*[@class="btn"]')
            time.sleep(1)
            self.driver.element.click("//span[text()='Claim']")
            time.sleep(5)
            self.wallet.suiWallet()
            notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
            textFile.write_txt_data(adsNum + ':OmniBTC1' + notion)
        except BaseException:
            pass

        self.driver.browser.navi_to_page('https://suia.io/brands/Sui%20Global')
        time.sleep(10)
        self.driver.element.click('(//*[@class="btn"])[1]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':Sui Global12' + notion)
        time.sleep(10)
        self.driver.element.click('(//*[@class="btn"])[1]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('(//*[@class="btn disabled"])[2]')
        textFile.write_txt_data(adsNum + ':Sui Global23' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/Sui%20Ecosystem')
        time.sleep(5)
        self.driver.element.click('(//*[@class="btn"])[1]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':Sui Ecosystem14' + notion)
        time.sleep(10)
        self.driver.element.click('(//*[@class="btn"])[1]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('(//*[@class="btn disabled"])[2]')
        textFile.write_txt_data(adsNum + ':Sui Ecosystem25' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/Mynft')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':Mynft6' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/Cetus')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':Cetus7' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/4EVERLAND')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':4EVERLAND8' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/BeLaunch')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':BeLaunch9' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/TokenPocket')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':TokenPocket10' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/Tocen%20Launchpad')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('(//*[@class="btn disabled"])[2]')
        textFile.write_txt_data(adsNum + ':Tocen Launchpad11' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/Foxiverse')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('(//*[@class="btn disabled"])[2]')
        textFile.write_txt_data(adsNum + ':Foxiverse12' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/MoveBit')
        time.sleep(5)
        self.driver.element.click('(//*[@class="btn"])[2]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('(//*[@class="btn disabled"])[1]')
        textFile.write_txt_data(adsNum + ':MoveBit13' + notion)

        self.driver.browser.navi_to_page('https://suia.io/brands/Sui.Love')
        time.sleep(5)
        self.driver.element.click('//*[@class="btn"]')
        time.sleep(1)
        self.driver.element.click("//span[text()='Claim']")
        time.sleep(5)
        self.wallet.suiWallet()
        notion = self.driver.element.get_text_60sec('//*[@class="btn disabled"]')
        textFile.write_txt_data(adsNum + ':Sui.Love14' + notion)

    def fleek(self, adsMail, adsNum):
        self.driver.browser.navi_to_page("https://fleek.xyz/")
        time.sleep(5)
        self.driver.browser.refresh()
        time.sleep(10)
        self.driver.element.click("//p[@class='framer-text']")
        time.sleep(1)
        self.driver.element.send_keys("//input[@data-name='email']", adsMail)
        time.sleep(10)
        self.driver.element.click("//button[@type='submit']")
        notion = self.driver.element.get_text_60sec('//div[@style="display: block;"]')
        textFile.write_txt_data(adsNum + notion)
        time.sleep(3)

    def zeta6(self, adsAddress):
        self.driver.browser.navi_to_page("https://docs.google.com/forms/d/e/1FAIpQLSd_cVX_CArycdutWIL70jQZPtPt3kdNtjYw8iDP8khKXivNAg/viewform")
        time.sleep(10)
        self.driver.element.send_keys("//input[@dir='auto']", adsAddress)
        time.sleep(1)
        self.driver.element.click("//span[text()='All the above (and any existing & future chain!)']")
        time.sleep(1)
        self.driver.element.click("//span[text()='Omnichain decentralized app']")
        time.sleep(1)
        self.driver.element.click("//span[text()='Access and manage assets, data, and liquidity on any chain']")
        time.sleep(1)
        self.driver.element.click("//span[text()='All the above']")
        time.sleep(1)
        self.driver.element.click("//span[text()='Bitcoin']")
        time.sleep(1)
        self.driver.element.click("//span[text()='B.) One-way peg where the only native value that goes cross-chain is via the ZETA token. The user receives the desired native asset in one swap.']")
        time.sleep(1)
        self.driver.element.click("//span[text()='All the above & much more!']")
        time.sleep(1)
        self.driver.element.click("//div[@role='button']//span")
        time.sleep(5)

    def glaxe_zeta(self, adsNum):
        self.driver.browser.navi_to_page("https://galxe.com/ZetaChain/campaign/GCormU4Rky")
        time.sleep(10)
        try:
            self.driver.element.click_3sec("//span[text()[normalize-space()='Switch to POLYGON']]")
            time.sleep(5)
            self.wallet.metamask_switch()
        except BaseException:
            pass
        try:
            self.driver.element.click("//span[@class='v-btn__content']")
            notion = self.driver.element.get_text_60sec("//div[text()[normalize-space()='Claim Successful!']]")
            print(adsNum + notion)
        except BaseException:
            print(adsNum + "失败")
            pass

    def sui(self, password):
        self.driver.browser.navi_to_page("chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html")
        time.sleep(2)
        self.driver.element.send_keys('//*[@id="root"]/div/div/div[2]/main/div/form/label/input', password)
        time.sleep(2)
        self.driver.element.click('//*[@id="root"]/div/div/div[2]/main/div/form/button')
        time.sleep(3)

        self.driver.element.click('//*[@data-testid="menu"]')
        self.driver.element.click('//div[text()="Network"]')
        self.driver.element.click('//*[text()="Sui Testnet"]')
        self.driver.element.click('//*[@id="root"]/div/div/div[1]/a[2]/span[1]')
