import time
from random import choice

from taskCode.actions import actionsBase
from taskCode.actions.textFile import textFile
from taskCode.config.dictumText import dictumText


class Twitter:
    def __init__(self, driver):
        self.driver = actionsBase(driver)

    # 封装推特关注功能
    def twitter_follow(self, url):
        self.driver.browser.navi_to_page(url)
        time.sleep(5)
        self.driver.element.click("//span[text()='关注']")
        time.sleep(3)

    # 封装推特点赞，转推功能
    def twitter_RT(self, url):
        self.driver.browser.navi_to_page(url)
        time.sleep(5)
        # //*[@id="id__9oxbqw381hn"]/div[3]/div/div/div/svg
        self.driver.element.click('//*[contains(@id,"__")]/div[3]/div[1]/div[1]/div[1]/div[1]')
        self.driver.element.click('//*[contains(@id,"__")]/div[2]/div[1]/div[1]/div[1]/div[1]')
        self.driver.element.click(
            '//div[@id="layers"]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]')

    def twitter_msg(self, adsAddress):
        self.driver.browser.navi_to_page('https://twitter.com/liangxied/status/1586863551087403008')
        time.sleep(5)
        self.driver.element.click("(//div[contains(@class,'css-901oao r-18jsvk2')]//div)[3]")
        self.driver.element.send_keys("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']", adsAddress)
        time.sleep(3)
        self.driver.element.click("//span[text()='回复']")

    def twitter_task(self, acd):
        self.twitter_RT('https://twitter.com/owangenft/status/1587519847168098306')
        time.sleep(3)
        self.twitter_follow('https://twitter.com/Apeironnft')
        time.sleep(5)
        self.twitter_follow('https://twitter.com/OwangeNFT')
        time.sleep(5)
        self.twitter_follow('https://twitter.com/OwangeToshiro')
        time.sleep(5)

        self.driver.browser.navi_to_page('https://www.premint.xyz/Apeiron-OwangeNFT/')
        time.sleep(3)
        self.driver.element.click('//*[@id="register-submit"]')
        notion = self.driver.element.get_text_60sec('//*[@id="registration_status"]/div/div')
        print(acd, notion)

    # 推特发推功能
    def sendTwitter(self, adsNum):
        # choice随机从列表中取值
        text = choice(dictumText)
        self.driver.browser.close_page()
        self.driver.browser.navi_to_page('https://twitter.com/home')
        time.sleep(5)
        try:
            self.driver.element.click("//a[@data-testid='SideNav_NewTweet_Button']")
            time.sleep(5)
            try:
                self.driver.element.click(
                    '//*[@id="layers"]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div/span')
            except BaseException:
                pass
            self.driver.element.click("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
            self.driver.element.send_keys(
                "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']", text)
            self.driver.element.click("//div[@data-testid='tweetButton']")
        except BaseException:
            notion = adsNum + '发推失败'
            textFile.write_txt_data(notion)
