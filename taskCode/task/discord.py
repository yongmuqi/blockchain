import time

from taskCode.actions import actionsBase
from taskCode.actions.baidu import Baidu


class Discord:
    # discord页面元素
    discord_imagepath = 'C:\\Users\\chencheng\\PycharmProjects\\adsTask\\taskCode\\image\\image'
    discord_text = 'Choose your answer here'

    def __init__(self, driver):
        self.driver = actionsBase(driver)

    # discord答题任务
    def discord_answer(self, img1, img2, url, x, y):
        # 打开DISCORD答题页面
        self.driver.browser.navi_to_page(url)
        time.sleep(15)
        timestring = time.strftime('%Y-%m-%d-')
        # 获取当前屏幕截图，并保存第一个截图
        self.driver.browser.screenshot(img1)
        imagepath = self.discord_imagepath + timestring + img1
        # 判断第一个截图和第一个问题的坐标
        offset = Baidu.baidu_return_cordinate(self.discord_text, imagepath)
        # 点击第一个问题
        self.driver.mouse.offset_click(offset[1], offset[0])
        time.sleep(3)
        # 通过X来点击第一个问题的答案
        answer = offset[0] + x * 40
        self.driver.mouse.offset_click(offset[1], answer)
        time.sleep(5)
        # 获取当前屏幕截图，并保存第二个截图
        self.driver.browser.screenshot(img2)
        imagepath = self.discord_imagepath + timestring + img2
        # 判断第二个截图和第二个问题的坐标
        offset = Baidu.baidu_return_cordinate(self.discord_text, imagepath)
        self.driver.mouse.offset_click(offset[1], offset[0])
        time.sleep(3)
        # 通过Y来点击第二个问题的答案
        answer = offset[0] + y * 40
        self.driver.mouse.offset_click(offset[1], answer)
        time.sleep(5)
