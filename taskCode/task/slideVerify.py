import random

import cv2
import numpy as np
import requests
from PIL import Image


class slideVerify:
    def __init__(self, driver):
        self.driver = driver

    def get_img_offset(self):
        # 下载验证码的背景图和滑块图
        background = self.driver.find.xpath_element("//div[@_id='im']").value_of_css_property("background-image")
        slide = self.driver.find.xpath_element("//div[@_id='shim']").value_of_css_property("background-image")
        image_url = background.split("\"")[1]
        slide_url = slide.split("\"")[1]
        r = requests.get(image_url)
        with open('image\\coinmarketcap\\back_ground.jpg', 'wb') as f:
            f.write(r.content)
        t = requests.get(slide_url)
        with open('image\\coinmarketcap\\slide_pic.jpg', 'wb') as fp:
            fp.write(t.content)
        back_img = "image\\coinmarketcap\\back_ground.jpg"
        img = Image.open("image\\coinmarketcap\\slide_pic.jpg")
        region = img.crop((0, 0, 60, 192))
        region.save("image\\coinmarketcap\\slide_pic1.png")
        slide_img = "image\\coinmarketcap\\slide_pic1.png"
        block = cv2.imread(slide_img, 0)
        template = cv2.imread(back_img, 0)
        w, h = block.shape[::-1]
        # 二值化后的图片
        block_name = 'image\\coinmarketcap\\block.jpg'
        template_name = 'image\\coinmarketcap\\template.jpg'
        # 保存二值化后的图片
        cv2.imwrite(block_name, block)
        cv2.imwrite(template_name, template)
        # 将滑块图片灰度化
        block = cv2.imread(block_name)
        block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
        # 反转block的值
        block = abs(255 - block)
        cv2.imwrite(block_name, block)
        block = cv2.imread(block_name)
        template = cv2.imread(template_name)
        # 获取偏移量
        # 模板匹配，查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
        result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(), result.shape)
        print(x, y)
        offset = y - 30
        # 画矩形圈出匹配的区域
        # 参数解释：1.原图 2.矩阵的左上点坐标 3.矩阵的右下点坐标 4.画线对应的rgb颜色 5.线的宽度
        site = cv2.rectangle(template, (y, x), (y + w, x + h), (7, 249, 151), 2)
        cv2.imwrite("image\\coinmarketcap\\paint.jpg", site)
        return offset

    def get_track(self, offset):
        track = []
        current = 0
        mid = offset * 3 / 4
        t = random.randint(2, 3) / 10
        v = 0
        while current < offset:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t
            current += move
            track.append(round(move, 2))
        return track